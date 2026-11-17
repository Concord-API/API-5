from datetime import date

from radar.collect import build_snapshot
from radar.sprints import Sprint

SPRINTS = [Sprint(3, date(2026, 11, 2), date(2026, 11, 22))]


def issue_item(item_id, number, title, status=None, status_since=None, closed_at=None, assignees=(), sprint=None):
    return {
        "id": item_id,
        "type": "ISSUE",
        "content": {
            "number": number,
            "title": title,
            "state": "CLOSED" if closed_at else "OPEN",
            "createdAt": "2026-11-03T13:00:00Z",
            "closedAt": closed_at,
            "assignees": {"nodes": [{"login": login} for login in assignees]},
            "issueFieldValues": {"nodes": [{"name": "Alta", "field": {"name": "Prioridade"}}]
                                 + ([{"name": sprint, "field": {"name": "Sprint"}}] if sprint else [])},
        },
        "status": {"name": status, "updatedAt": status_since} if status else None,
        "radar": None,
        "semana": None,
        "etapa": None,
        "valor": None,
        "dias": None,
    }


def metric_item(item_id, semana, etapa, valor):
    return {
        "id": item_id,
        "type": "DRAFT_ISSUE",
        "content": {"title": f"{etapa} · {semana}", "assignees": {"nodes": []}},
        "status": None,
        "radar": {"name": "Métrica"},
        "semana": {"name": semana},
        "etapa": {"name": etapa},
        "valor": {"number": valor},
        "dias": None,
    }


def commit(oid, authored, parents=1, login=None):
    author = {"user": {"login": login, "id": f"U_{login}"}} if login else {"user": None}
    return {"commit": {"oid": oid, "authoredDate": authored, "parents": {"totalCount": parents}, "author": author}}


def pull(number, branch, base, commits, reviews=(), merged_at=None):
    return {
        "number": number,
        "headRefName": branch,
        "baseRefName": base,
        "createdAt": "2026-11-06T10:00:00Z",
        "mergedAt": merged_at,
        "reviews": {"nodes": [{"submittedAt": at} for at in reviews]},
        "commits": {"nodes": commits},
    }


def snapshot(items=(), pulls=None):
    return build_snapshot(date(2026, 11, 16), SPRINTS, list(items), pulls or {})


def test_keeps_only_the_tasks_of_the_board():
    result = snapshot([
        issue_item("I1", 401, "27.3 Add the CSV export endpoint", "Todo", "2026-11-04T12:00:00Z", assignees=["ana"],
                   sprint="Sprint 3"),
        issue_item("I2", 327, "US-27 — As a user, I want to export to CSV"),
        issue_item("I3", 245, "DevOps"),
        issue_item("I4", 382, "DVP-70 Add the Radar workflow", "Done", "2026-11-15T12:00:00Z", closed_at="2026-11-15T12:00:00Z"),
    ])

    assert [task["task"] for task in result["tasks"]] == ["27.3", "DVP-70"]
    first = result["tasks"][0]
    assert first == {
        "item_id": "I1",
        "number": 401,
        "task": "27.3",
        "story": "US-27",
        "title": "27.3 Add the CSV export endpoint",
        "state": "OPEN",
        "created_at": "2026-11-03T13:00:00Z",
        "closed_at": None,
        "status": "Todo",
        "status_since": "2026-11-04T12:00:00Z",
        "assignees": ["ana"],
        "sprint": 3,
        "days_in_status": None,
    }
    assert result["tasks"][1]["sprint"] is None


def test_keeps_the_metric_items_apart_from_the_tasks():
    result = snapshot([metric_item("M1", "S3·1", "Commits", 44)])

    assert result["tasks"] == []
    assert result["metrics"] == [{"item_id": "M1", "semana": "S3·1", "etapa": "Commits", "valor": 44, "pessoa": None}]


def test_links_each_pull_request_to_its_task_with_first_commit_and_first_review():
    result = snapshot(pulls={"API5-Backend": [
        pull(51, "27.3-Add-the-CSV-export-endpoint", "us27",
             [commit("b", "2026-11-06T09:00:00Z"), commit("a", "2026-11-05T09:00:00Z")],
             reviews=["2026-11-08T10:00:00Z", "2026-11-07T10:00:00Z"],
             merged_at="2026-11-09T10:00:00Z"),
    ]})

    assert result["pulls"] == [{
        "repo": "API5-Backend",
        "number": 51,
        "branch": "27.3-Add-the-CSV-export-endpoint",
        "base": "us27",
        "task": "27.3",
        "created_at": "2026-11-06T10:00:00Z",
        "merged_at": "2026-11-09T10:00:00Z",
        "first_commit_at": "2026-11-05T09:00:00Z",
        "first_review_at": "2026-11-07T10:00:00Z",
    }]


def test_counts_each_commit_once_without_merge_commits():
    result = snapshot(pulls={"API5-Frontend": [
        pull(10, "27.4-Add-the-export-button", "us27",
             [commit("a", "2026-11-05T09:00:00Z", login="ana"), commit("m", "2026-11-05T10:00:00Z", parents=2)]),
        pull(11, "us27", "main",
             [commit("a", "2026-11-05T09:00:00Z"), commit("c", "2026-11-06T09:00:00Z")]),
    ]})

    assert result["commits"] == [
        {"repo": "API5-Frontend", "sha": "a", "date": "2026-11-05T09:00:00Z", "task": "27.4",
         "author": "ana", "author_id": "U_ana"},
        {"repo": "API5-Frontend", "sha": "c", "date": "2026-11-06T09:00:00Z", "task": None,
         "author": None, "author_id": None},
    ]


def test_records_the_day_and_the_sprint_windows():
    result = snapshot()

    assert result["date"] == "2026-11-16"
    assert result["sprints"] == [{"number": 3, "start": "2026-11-02", "end": "2026-11-22"}]


def test_keeps_the_person_of_a_metric_item():
    item = metric_item("M2", "S3", "Commits por pessoa", 12)
    item["content"]["assignees"]["nodes"] = [{"login": "ana"}]

    assert snapshot([item])["metrics"][0]["pessoa"] == "ana"
