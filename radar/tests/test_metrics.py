from datetime import date, datetime, timezone

from radar.board import Metric
from radar.metrics import stage_metrics, week_metrics, weeks
from radar.sprints import Sprint

TZ = "America/Sao_Paulo"
S1 = Sprint(1, date(2026, 9, 7), date(2026, 9, 27))
S2 = Sprint(2, date(2026, 10, 5), date(2026, 10, 25))


def task(created, number=1, task_id="2.1", state="OPEN", closed=None, sprint=None):
    return {"number": number, "task": task_id, "created_at": created, "state": state, "closed_at": closed,
            "sprint": sprint}


def pull(task_id, created, first_commit=None, first_review=None, merged=None, base="us2"):
    return {"task": task_id, "base": base, "created_at": created, "first_commit_at": first_commit,
            "first_review_at": first_review, "merged_at": merged}


def snapshot(tasks=(), pulls=(), commits=()):
    return {"tasks": list(tasks), "pulls": list(pulls), "commits": list(commits)}


def test_each_sprint_has_a_planning_week_before_it_and_three_weeks_inside():
    assert weeks([S1], date(2026, 10, 1)) == [
        ("S1·0 planning", date(2026, 8, 31), date(2026, 9, 6)),
        ("S1·1", date(2026, 9, 7), date(2026, 9, 13)),
        ("S1·2", date(2026, 9, 14), date(2026, 9, 20)),
        ("S1·3", date(2026, 9, 21), date(2026, 9, 27)),
    ]


def test_weeks_that_did_not_start_yet_are_left_out():
    assert [label for label, _, _ in weeks([S1], date(2026, 9, 14))] == ["S1·0 planning", "S1·1", "S1·2"]


def test_counts_tasks_created_and_commits_of_each_week_in_local_time():
    data = snapshot(
        tasks=[task("2026-09-22T15:00:00Z"), task("2026-09-23T15:00:00Z", 2, "2.2")],
        commits=[
            {"date": "2026-09-15T12:00:00Z"},
            {"date": "2026-09-28T01:30:00Z"},
            {"date": "2026-09-28T12:00:00Z"},
        ],
    )

    metrics = week_metrics(data, [S1], date(2026, 9, 27), TZ)

    assert Metric("S1·3", "Tasks criadas", 2) in metrics
    assert Metric("S1·2", "Commits", 1) in metrics
    assert Metric("S1·3", "Commits", 1) in metrics
    assert Metric("S1·1", "Commits", 0) in metrics
    assert len(metrics) == 8


def test_a_task_created_in_the_planning_week_counts_in_the_next_sprint():
    data = snapshot(
        tasks=[task("2026-10-01T12:00:00Z", task_id="3.1")],
        pulls=[pull("3.1", "2026-10-06T12:00:00Z", first_commit="2026-10-05T12:00:00Z",
                    merged="2026-10-07T12:00:00Z")],
    )

    metrics = stage_metrics(data, [S1, S2], datetime(2026, 10, 26, tzinfo=timezone.utc), TZ)

    assert Metric("S2", "Esperando começar", 4) in metrics
    assert Metric("S1", "Esperando começar", 0) in metrics


def test_sums_the_days_of_each_stage_from_issue_to_merge():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", state="CLOSED", closed="2026-09-20T12:00:00Z")],
        pulls=[pull("2.1", "2026-09-14T12:00:00Z", first_commit="2026-09-12T12:00:00Z",
                    first_review="2026-09-17T12:00:00Z", merged="2026-09-18T12:00:00Z")],
    )

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 27, tzinfo=timezone.utc), TZ)

    assert set(metrics) == {
        Metric("S1", "Esperando começar", 4),
        Metric("S1", "Desenvolvendo", 2),
        Metric("S1", "Esperando revisão", 3),
        Metric("S1", "Nunca começou", 0),
    }


def test_a_pull_request_without_review_waits_until_the_merge_or_until_now():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z"), task("2026-09-08T12:00:00Z", 2, "2.2")],
        pulls=[
            pull("2.1", "2026-09-10T12:00:00Z", first_commit="2026-09-10T12:00:00Z", merged="2026-09-12T12:00:00Z"),
            pull("2.2", "2026-09-20T12:00:00Z", first_commit="2026-09-20T12:00:00Z"),
        ],
    )

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 25, 12, tzinfo=timezone.utc), TZ)

    assert Metric("S1", "Esperando revisão", 7) in metrics


def test_an_open_task_without_pull_request_never_started_and_a_closed_one_is_left_out():
    data = snapshot(tasks=[
        task("2026-09-08T12:00:00Z"),
        task("2026-09-08T12:00:00Z", 2, "2.2", state="CLOSED", closed="2026-09-09T12:00:00Z"),
    ])

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 18, 12, tzinfo=timezone.utc), TZ)

    assert Metric("S1", "Nunca começou", 10) in metrics
    assert Metric("S1", "Esperando começar", 0) in metrics


def test_pull_requests_into_main_do_not_count_as_task_work():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", task_id="0.5")],
        pulls=[pull("0.5", "2026-09-10T12:00:00Z", first_commit="2026-09-09T12:00:00Z", base="main")],
    )

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 18, 12, tzinfo=timezone.utc), TZ)

    assert Metric("S1", "Nunca começou", 10) in metrics


def test_a_pull_request_closed_without_merge_does_not_keep_the_task_waiting():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", state="CLOSED", closed="2026-09-12T12:00:00Z")],
        pulls=[
            pull("2.1", "2026-09-09T12:00:00Z", first_commit="2026-09-09T12:00:00Z"),
            pull("2.1", "2026-09-10T12:00:00Z", first_commit="2026-09-10T12:00:00Z", merged="2026-09-12T12:00:00Z"),
        ],
    )

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 27, tzinfo=timezone.utc), TZ)

    assert Metric("S1", "Esperando revisão", 3) in metrics


def test_a_task_split_in_pull_requests_starts_at_the_first_commit_and_ends_at_the_last_merge():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z")],
        pulls=[
            pull("2.1", "2026-09-12T12:00:00Z", first_commit="2026-09-11T12:00:00Z", merged="2026-09-13T12:00:00Z"),
            pull("2.1", "2026-09-14T12:00:00Z", first_commit="2026-09-10T12:00:00Z", merged="2026-09-16T12:00:00Z"),
        ],
    )

    metrics = stage_metrics(data, [S1], datetime(2026, 9, 27, tzinfo=timezone.utc), TZ)

    assert Metric("S1", "Esperando começar", 2) in metrics
    assert Metric("S1", "Desenvolvendo", 2) in metrics
    assert Metric("S1", "Esperando revisão", 4) in metrics


def test_a_task_counts_in_the_sprint_of_its_sprint_field_and_not_of_its_creation():
    data = snapshot(tasks=[task("2026-10-06T12:00:00Z", task_id="DVP-14", sprint=3)])
    s3 = Sprint(3, date(2026, 11, 2), date(2026, 11, 22))

    metrics = stage_metrics(data, [S1, S2, s3], datetime(2026, 11, 16, 12, tzinfo=timezone.utc), TZ)

    assert Metric("S2", "Nunca começou", 0) in metrics
    assert Metric("S3", "Nunca começou", 41) in metrics


def test_a_task_without_sprint_field_counts_in_the_sprint_of_its_creation():
    data = snapshot(tasks=[task("2026-10-06T12:00:00Z", task_id="DVP-14")])

    metrics = stage_metrics(data, [S1, S2], datetime(2026, 10, 16, 12, tzinfo=timezone.utc), TZ)

    assert Metric("S2", "Nunca começou", 10) in metrics
