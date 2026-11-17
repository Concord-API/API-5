from datetime import date, datetime, timezone

from radar.board import Metric
from radar.metrics import FIRST_COMMIT, OPEN_PR, REVIEW, created_in, person_metrics, task_times, week_metrics, weeks
from radar.sprints import Sprint

TZ = "America/Sao_Paulo"
S1 = Sprint(1, date(2026, 9, 7), date(2026, 9, 27))
S2 = Sprint(2, date(2026, 10, 5), date(2026, 10, 25))


def task(created, number=1, task_id="2.1", state="OPEN", closed=None):
    return {"item_id": f"I{number}", "number": number, "task": task_id, "created_at": created, "state": state,
            "closed_at": closed}


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


def times(data, now):
    return task_times(data, now)


def test_measures_each_stage_of_a_task_from_issue_to_merge():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", state="CLOSED", closed="2026-09-20T12:00:00Z")],
        pulls=[pull("2.1", "2026-09-14T12:00:00Z", first_commit="2026-09-12T12:00:00Z",
                    first_review="2026-09-17T12:00:00Z", merged="2026-09-18T12:00:00Z")],
    )

    assert times(data, datetime(2026, 9, 27, tzinfo=timezone.utc)) == {"I1": {FIRST_COMMIT: 4, OPEN_PR: 2, REVIEW: 3}}


def test_a_pull_request_without_review_waits_until_now():
    data = snapshot(
        tasks=[task("2026-09-18T12:00:00Z")],
        pulls=[pull("2.1", "2026-09-20T12:00:00Z", first_commit="2026-09-20T12:00:00Z")],
    )

    assert times(data, datetime(2026, 9, 25, 12, tzinfo=timezone.utc))["I1"][REVIEW] == 5


def test_an_open_task_without_pull_request_is_still_waiting_for_its_first_commit():
    data = snapshot(tasks=[task("2026-09-08T12:00:00Z")])

    assert times(data, datetime(2026, 9, 18, 12, tzinfo=timezone.utc)) == {
        "I1": {FIRST_COMMIT: 10, OPEN_PR: None, REVIEW: None}}


def test_a_closed_task_without_pull_request_has_no_times():
    data = snapshot(tasks=[task("2026-09-08T12:00:00Z", state="CLOSED", closed="2026-09-09T12:00:00Z")])

    assert times(data, datetime(2026, 9, 18, 12, tzinfo=timezone.utc)) == {
        "I1": {FIRST_COMMIT: None, OPEN_PR: None, REVIEW: None}}


def test_pull_requests_into_main_do_not_count_as_task_work():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", task_id="0.5")],
        pulls=[pull("0.5", "2026-09-10T12:00:00Z", first_commit="2026-09-09T12:00:00Z", base="main")],
    )

    assert times(data, datetime(2026, 9, 18, 12, tzinfo=timezone.utc))["I1"][FIRST_COMMIT] == 10


def test_a_pull_request_closed_without_merge_does_not_keep_the_task_waiting():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z", state="CLOSED", closed="2026-09-12T12:00:00Z")],
        pulls=[
            pull("2.1", "2026-09-09T12:00:00Z", first_commit="2026-09-09T12:00:00Z"),
            pull("2.1", "2026-09-10T12:00:00Z", first_commit="2026-09-10T12:00:00Z", merged="2026-09-12T12:00:00Z"),
        ],
    )

    assert times(data, datetime(2026, 9, 27, tzinfo=timezone.utc))["I1"][REVIEW] == 3


def test_a_task_split_in_pull_requests_starts_at_the_first_commit_and_ends_at_the_last_merge():
    data = snapshot(
        tasks=[task("2026-09-08T12:00:00Z")],
        pulls=[
            pull("2.1", "2026-09-12T12:00:00Z", first_commit="2026-09-11T12:00:00Z", merged="2026-09-13T12:00:00Z"),
            pull("2.1", "2026-09-14T12:00:00Z", first_commit="2026-09-10T12:00:00Z", merged="2026-09-16T12:00:00Z"),
        ],
    )

    assert times(data, datetime(2026, 9, 27, tzinfo=timezone.utc)) == {"I1": {FIRST_COMMIT: 2, OPEN_PR: 2, REVIEW: 4}}


S3 = Sprint(3, date(2026, 11, 2), date(2026, 11, 22))


def test_tells_when_a_task_was_created_compared_to_its_sprint():
    tasks = {
        "antes": {"created_at": "2026-10-30T12:00:00Z", "sprint": 3},
        "semana1": {"created_at": "2026-11-02T12:00:00Z", "sprint": 3},
        "semana3": {"created_at": "2026-11-17T01:00:00Z", "sprint": 3},
        "depois": {"created_at": "2026-11-25T12:00:00Z", "sprint": 3},
        "sem sprint": {"created_at": "2026-11-03T12:00:00Z", "sprint": None},
        "sprint sem janela": {"created_at": "2026-11-03T12:00:00Z", "sprint": 4},
    }

    result = {name: created_in(task, [S1, S2, S3], TZ) for name, task in tasks.items()}

    assert result == {
        "antes": "Antes do início",
        "semana1": "Semana 1",
        "semana3": "Semana 3",
        "depois": "Depois do fim",
        "sem sprint": "Semana 1",
        "sprint sem janela": None,
    }


def test_counts_the_commits_of_each_person_in_each_sprint_including_its_planning_week():
    data = snapshot(commits=[
        {"date": "2026-10-28T12:00:00Z", "author": "ana", "author_id": "U1"},
        {"date": "2026-11-03T12:00:00Z", "author": "ana", "author_id": "U1"},
        {"date": "2026-11-04T12:00:00Z", "author": "bia", "author_id": "U2"},
        {"date": "2026-10-20T12:00:00Z", "author": "bia", "author_id": "U2"},
        {"date": "2026-11-04T12:00:00Z", "author": None, "author_id": None},
    ])

    metrics = person_metrics(data, [S2, S3], date(2026, 11, 16), TZ)

    assert sorted((m.semana, m.pessoa, m.valor) for m in metrics) == [
        ("S2", "bia", 1), ("S3", "ana", 2), ("S3", "bia", 1)]
    assert all(m.etapa == "Commits por pessoa" for m in metrics)
