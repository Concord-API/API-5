from datetime import date

from radar.links import story_of, task_from_branch, task_from_title
from radar.sprints import Sprint

METRIC = "Métrica"


def _value(node, key):
    return node[key] if node else None


def _task(item):
    content = item["content"]
    task = task_from_title(content["title"])
    if item["type"] != "ISSUE" or not task:
        return None
    return {
        "item_id": item["id"],
        "number": content["number"],
        "task": task,
        "story": story_of(task),
        "title": content["title"],
        "state": content["state"],
        "created_at": content["createdAt"],
        "closed_at": content["closedAt"],
        "status": _value(item["status"], "name"),
        "status_since": _value(item["status"], "updatedAt"),
        "assignees": [node["login"] for node in content["assignees"]["nodes"]],
        "days_in_status": None,
    }


def _metric(item):
    return {
        "item_id": item["id"],
        "semana": _value(item["semana"], "name"),
        "etapa": _value(item["etapa"], "name"),
        "valor": _value(item["valor"], "number"),
    }


def _own_commits(pull):
    return [node["commit"] for node in pull["commits"]["nodes"] if node["commit"]["parents"]["totalCount"] < 2]


def _pull(repo, pull):
    commits = _own_commits(pull)
    reviews = [node["submittedAt"] for node in pull["reviews"]["nodes"] if node["submittedAt"]]
    return {
        "repo": repo,
        "number": pull["number"],
        "branch": pull["headRefName"],
        "base": pull["baseRefName"],
        "task": task_from_branch(pull["headRefName"]),
        "created_at": pull["createdAt"],
        "merged_at": pull["mergedAt"],
        "first_commit_at": min((c["authoredDate"] for c in commits), default=None),
        "first_review_at": min(reviews, default=None),
    }


def _commits(repo, pulls):
    seen = {}
    for pull in sorted(pulls, key=lambda p: task_from_branch(p["headRefName"]) is None):
        task = task_from_branch(pull["headRefName"])
        for commit in _own_commits(pull):
            if commit["oid"] not in seen:
                seen[commit["oid"]] = {"repo": repo, "sha": commit["oid"], "date": commit["authoredDate"], "task": task}
    return sorted(seen.values(), key=lambda c: (c["date"], c["sha"]))


def build_snapshot(today: date, sprints: list[Sprint], items: list[dict], pulls_by_repo: dict[str, list[dict]]) -> dict:
    tasks = [task for task in map(_task, items) if task]
    metrics = [_metric(item) for item in items if _value(item["radar"], "name") == METRIC]
    pulls = [_pull(repo, pull) for repo, pulls in pulls_by_repo.items() for pull in pulls]
    commits = [commit for repo, pulls in pulls_by_repo.items() for commit in _commits(repo, pulls)]
    return {
        "date": today.isoformat(),
        "sprints": [{"number": s.number, "start": s.start.isoformat(), "end": s.end.isoformat()} for s in sprints],
        "tasks": tasks,
        "metrics": metrics,
        "pulls": pulls,
        "commits": commits,
    }
