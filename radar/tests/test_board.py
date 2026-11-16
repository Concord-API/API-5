from datetime import date

from radar.board import Metric, days_in_status, plan_days, plan_metrics


def task(item_id, status, since, state="OPEN", days=None):
    return {"item_id": item_id, "status": status, "status_since": since, "state": state, "days_in_status": days}


def test_counts_whole_days_since_the_last_status_change_in_the_local_day():
    assert days_in_status("2026-11-12T02:30:00Z", date(2026, 11, 16), "America/Sao_Paulo") == 5
    assert days_in_status("2026-11-16T11:00:00Z", date(2026, 11, 16), "America/Sao_Paulo") == 0


def test_fills_the_days_of_open_tasks_that_are_not_done():
    tasks = [
        task("A", "Todo", "2026-11-04T15:00:00Z"),
        task("B", "Review", "2026-11-14T15:00:00Z"),
        task("C", "Done", "2026-11-10T15:00:00Z", state="CLOSED"),
        task("D", None, None),
    ]

    assert plan_days(tasks, {}, date(2026, 11, 16), "America/Sao_Paulo") == {"A": 12, "B": 2}


def test_does_not_rewrite_a_value_that_did_not_change():
    tasks = [task("A", "Todo", "2026-11-04T15:00:00Z"), task("B", "Review", "2026-11-14T15:00:00Z")]

    assert plan_days(tasks, {"A": 12, "B": 1}, date(2026, 11, 16), "America/Sao_Paulo") == {"B": 2}


def test_clears_the_days_of_a_task_that_left_the_open_columns():
    tasks = [
        task("C", "Done", "2026-11-10T15:00:00Z", state="CLOSED"),
        task("D", None, None),
        task("E", "Done", "2026-11-10T15:00:00Z", state="CLOSED"),
    ]

    assert plan_days(tasks, {"C": 4, "D": 1}, date(2026, 11, 16), "America/Sao_Paulo") == {"C": None, "D": None}


def test_creates_only_the_metrics_that_are_not_on_the_board():
    existing = [{"item_id": "M1", "semana": "S3·1", "etapa": "Commits", "valor": 44}]
    metrics = [Metric("S3·1", "Commits", 44), Metric("S3·1", "Tasks criadas", 38)]

    creates, updates = plan_metrics(existing, metrics)

    assert creates == [Metric("S3·1", "Tasks criadas", 38)]
    assert updates == []


def test_updates_the_value_of_a_metric_that_is_already_on_the_board():
    existing = [{"item_id": "M1", "semana": "S3·2", "etapa": "Commits", "valor": 10}]

    creates, updates = plan_metrics(existing, [Metric("S3·2", "Commits", 12)])

    assert creates == []
    assert updates == [("M1", Metric("S3·2", "Commits", 12))]


def test_the_title_names_the_stage_and_the_week():
    assert Metric("Planning S3", "Commits", 50).title == "Commits · Planning S3"
