from datetime import date

from radar.alerts import (
    Rules, business_days, current_sprint, last_commits, next_step, plan_alerts, render,
)
from radar.sprints import Sprint

TZ = "America/Sao_Paulo"
S3 = Sprint(3, date(2026, 11, 2), date(2026, 11, 22))
S4 = Sprint(4, date(2026, 11, 30), date(2026, 12, 20))
RULES = Rules(master="joao", team=["ana", "bia", "caio", "joao", "vini"], no_task_expected=["vini"])


def task(number, story="US-21", assignees=(), sprint=4, state="OPEN", status="Todo"):
    return {"number": number, "story": story, "assignees": list(assignees), "sprint": sprint, "state": state,
            "status": status}


def story(label, sprint=4, state="OPEN"):
    return {"number": 100, "story": label, "sprint": sprint, "state": state}


def snapshot(tasks=(), stories=()):
    return {"tasks": list(tasks), "stories": list(stories)}


def test_counts_only_the_weekdays_after_a_day():
    assert business_days(date(2026, 12, 4), date(2026, 12, 7)) == 1
    assert business_days(date(2026, 12, 1), date(2026, 12, 3)) == 2
    assert business_days(date(2026, 12, 3), date(2026, 12, 3)) == 0


def test_there_is_no_sprint_before_the_start_and_after_the_end():
    assert current_sprint([S3, S4], date(2026, 11, 25)) is None
    assert current_sprint([S3, S4], date(2026, 12, 20)) == S4
    assert current_sprint([S3, S4], date(2026, 12, 21)) is None


def test_keeps_the_last_local_day_each_person_committed():
    commits = [
        {"date": "2026-12-01T12:00:00Z", "author": "ana"},
        {"date": "2026-12-03T01:00:00Z", "author": "ana"},
        {"date": "2026-12-02T12:00:00Z", "author": None},
    ]

    assert last_commits(commits, TZ) == {"ana": date(2026, 12, 2)}


def test_charges_a_person_with_a_task_who_did_not_commit_in_any_task():
    data = snapshot([task(45, assignees=["ana"]), task(52, assignees=["ana"]), task(60, assignees=["bia"])])
    commits = {"ana": date(2026, 12, 1), "bia": date(2026, 12, 3)}

    alerts = plan_alerts(data, S4, date(2026, 12, 4), RULES, commits)

    assert alerts["idle"] == [{"login": "ana", "days": 3, "tasks": [45, 52], "escalate": False}]


def test_counts_the_days_from_the_sprint_start_when_the_person_never_committed_in_it():
    data = snapshot([task(45, assignees=["ana"])])

    alerts = plan_alerts(data, S4, date(2026, 12, 4), RULES, {"ana": date(2026, 11, 20)})

    assert alerts["idle"] == [{"login": "ana", "days": 4, "tasks": [45], "escalate": True}]


def test_does_not_charge_who_committed_less_than_two_weekdays_ago():
    data = snapshot([task(45, assignees=["ana"])])

    assert plan_alerts(data, S4, date(2026, 12, 7), RULES, {"ana": date(2026, 12, 4)})["idle"] == []


def test_done_closed_and_other_sprint_tasks_do_not_count_as_a_task_in_the_name():
    data = snapshot([
        task(45, assignees=["ana"], status="Done"),
        task(46, assignees=["ana"], state="CLOSED"),
        task(47, assignees=["ana"], sprint=3),
    ], [story("US-21")])

    alerts = plan_alerts(data, S4, date(2026, 12, 9), RULES, {})

    assert alerts["idle"] == []
    assert "ana" in alerts["without_task"]


def test_people_without_a_task_are_charged_to_the_master_except_who_is_not_expected_to_have_one():
    data = snapshot([task(45, assignees=["ana"]), task(46, assignees=["vini"])], [story("US-21")])

    alerts = plan_alerts(data, S4, date(2026, 12, 1), RULES, {})

    assert alerts["without_task"] == ["bia", "caio", "joao"]
    assert [person["login"] for person in alerts["idle"]] == []


def test_the_product_owner_is_charged_when_he_has_a_task():
    data = snapshot([task(46, assignees=["vini"])])

    alerts = plan_alerts(data, S4, date(2026, 12, 3), RULES, {})

    assert alerts["idle"] == [{"login": "vini", "days": 3, "tasks": [46], "escalate": False}]


def test_lists_the_tasks_without_anyone_and_the_stories_without_tasks():
    data = snapshot(
        tasks=[task(60), task(61, assignees=["ana"]), task(62, sprint=3), task(63, story="US-22")],
        stories=[story("US-21"), story("US-22"), story("US-23"), story("US-24", sprint=3),
                 story("US-25", state="CLOSED")],
    )

    alerts = plan_alerts(data, S4, date(2026, 12, 1), RULES, {})

    assert alerts["unassigned"] == [60, 63]
    assert alerts["stories_without_tasks"] == ["US-23"]


def test_the_message_mentions_who_is_stalled_and_the_master_and_never_who_has_no_task():
    alerts = {
        "idle": [{"login": "ana", "days": 3, "tasks": [45, 52], "escalate": False},
                 {"login": "bia", "days": 5, "tasks": [60], "escalate": True}],
        "unassigned": [61],
        "without_task": ["caio"],
        "stories_without_tasks": ["US-23"],
    }

    text = render(alerts, S4, date(2026, 12, 4), RULES)

    assert text.startswith("<!-- radar:2026-12-04 -->")
    assert "@ana, **3 dias úteis** sem commit, comentário ou card movido, com 2 tasks no nome: #45, #52" in text
    assert "@bia, **5 dias úteis** sem commit, comentário ou card movido, com 1 task no nome: #60 · @joao" in text
    assert "1 task sem ninguém: #61" in text
    assert "Sem task na sprint: `caio`" in text
    assert "@caio" not in text
    assert "US sem nenhuma task: US-23" in text


def test_the_message_says_when_nothing_is_stalled():
    alerts = {"idle": [], "unassigned": [], "without_task": [], "stories_without_tasks": []}

    assert "✅ Nenhuma trava hoje" in render(alerts, S4, date(2026, 12, 4), RULES)


def test_creates_the_issue_once_and_stops_while_it_is_closed():
    marker = "<!-- radar:2026-12-04 -->"

    assert next_step(None, marker) == "create"
    assert next_step({"state": "OPEN", "last_comment": "<!-- radar:2026-12-03 -->"}, marker) == "comment"
    assert next_step({"state": "OPEN", "last_comment": None}, marker) == "comment"
    assert next_step({"state": "OPEN", "last_comment": marker + "\n..."}, marker) == "already"
    assert next_step({"state": "CLOSED", "last_comment": None}, marker) == "paused"


def test_the_master_is_not_mentioned_twice_when_he_is_the_one_stalled():
    alerts = {"idle": [{"login": "joao", "days": 6, "tasks": [70], "escalate": True}],
              "unassigned": [], "without_task": [], "stories_without_tasks": []}

    text = render(alerts, S4, date(2026, 12, 8), RULES)

    assert "@joao, **6 dias úteis** sem commit, comentário ou card movido, com 1 task no nome: #70\n" in text


def test_nobody_is_listed_without_a_task_when_the_sprint_has_no_story():
    data = snapshot([task(45, story=None, assignees=["ana"])], [story("US-30", sprint=3)])

    assert plan_alerts(data, S4, date(2026, 12, 1), RULES, {})["without_task"] == []


def test_a_comment_or_a_status_change_on_a_task_counts_as_work_like_a_commit():
    activity = [
        {"date": "2026-12-03T12:00:00Z", "author": "ana"},
        {"date": "2026-12-04T15:00:00Z", "author": "bia"},
    ]
    commits = [{"date": "2026-12-01T12:00:00Z", "author": "ana"}]

    assert last_commits(commits + activity, TZ) == {"ana": date(2026, 12, 3), "bia": date(2026, 12, 4)}


def test_the_master_is_charged_while_the_started_sprint_has_no_task_at_all():
    data = snapshot([task(45, sprint=3)], [story("US-30", sprint=3)])

    alerts = plan_alerts(data, S4, date(2026, 12, 2), RULES, {})

    assert alerts["empty_sprint"] == 2
    assert "📭 A Sprint 4 começou há 2 dias úteis e não tem nenhuma task." in render(alerts, S4, date(2026, 12, 2), RULES)


def test_a_sprint_whose_tasks_are_all_done_is_not_empty():
    data = snapshot([task(45, assignees=["ana"], state="CLOSED", status="Done")])

    alerts = plan_alerts(data, S4, date(2026, 12, 2), RULES, {})

    assert alerts["empty_sprint"] is None
    assert "✅ Nenhuma trava hoje" in render(alerts, S4, date(2026, 12, 2), RULES)


def test_the_empty_sprint_says_when_it_started_today():
    alerts = plan_alerts(snapshot(), S4, date(2026, 11, 30), RULES, {})

    assert "📭 A Sprint 4 começou hoje e não tem nenhuma task." in render(alerts, S4, date(2026, 11, 30), RULES)
