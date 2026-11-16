from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

from radar.board import Metric
from radar.sprints import Sprint

WEEK = timedelta(days=7)
DAY = 86400
TASKS_CREATED = "Tasks criadas"
COMMITS = "Commits"
FIRST_COMMIT = "Dias até o 1º commit"
OPEN_PR = "Dias até abrir o PR"
REVIEW = "Dias esperando revisão"
TIME_FIELDS = [FIRST_COMMIT, OPEN_PR, REVIEW]


def _instant(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _local_day(value: str, timezone: str) -> date:
    return _instant(value).astimezone(ZoneInfo(timezone)).date()


def _days(start: datetime, end: datetime) -> float:
    return max(0.0, (end - start).total_seconds() / DAY)


def weeks(sprints: list[Sprint], today: date) -> list[tuple[str, date, date]]:
    result = []
    for sprint in sprints:
        planning = sprint.start - WEEK
        candidates = [(f"S{sprint.number}·0 planning", planning)]
        candidates += [(f"S{sprint.number}·{n}", sprint.start + WEEK * (n - 1)) for n in (1, 2, 3)]
        for label, start in candidates:
            if start <= today:
                result.append((label, start, start + timedelta(days=6)))
    return result


def _week_of(day: date, all_weeks: list[tuple[str, date, date]]) -> str | None:
    for label, start, end in all_weeks:
        if start <= day <= end:
            return label
    return None


def week_metrics(snapshot: dict, sprints: list[Sprint], today: date, timezone: str) -> list[Metric]:
    all_weeks = weeks(sprints, today)
    created = Counter(_week_of(_local_day(t["created_at"], timezone), all_weeks) for t in snapshot["tasks"])
    commits = Counter(_week_of(_local_day(c["date"], timezone), all_weeks) for c in snapshot["commits"])
    metrics = []
    for label, _, _ in all_weeks:
        metrics.append(Metric(label, TASKS_CREATED, created[label]))
        metrics.append(Metric(label, COMMITS, commits[label]))
    return metrics


def _pulls_by_task(snapshot: dict) -> dict[str, list[dict]]:
    pulls = defaultdict(list)
    for pull in snapshot["pulls"]:
        if pull["task"] and pull["base"] != "main":
            pulls[pull["task"]].append(pull)
    return pulls


def _rounded(days: float | None) -> int | None:
    return None if days is None else round(days)


def _times(task: dict, pulls: list[dict], now: datetime) -> dict[str, int | None]:
    created = _instant(task["created_at"])
    if not pulls:
        waiting = _days(created, now) if task["state"] == "OPEN" else None
        return {FIRST_COMMIT: _rounded(waiting), OPEN_PR: None, REVIEW: None}
    opened = min(_instant(p["created_at"]) for p in pulls)
    first_commit = min(_instant(p["first_commit_at"] or p["created_at"]) for p in pulls)
    merges = [_instant(p["merged_at"]) for p in pulls if p["merged_at"]]
    reviews = [_instant(p["first_review_at"]) for p in pulls if p["first_review_at"]]
    if merges:
        end = max(merges)
    elif task["closed_at"]:
        end = _instant(task["closed_at"])
    else:
        end = now
    review = min(reviews) if reviews else None
    waiting_until = review if review and review < end else end
    return {
        FIRST_COMMIT: _rounded(_days(created, first_commit)),
        OPEN_PR: _rounded(_days(first_commit, opened)),
        REVIEW: _rounded(_days(opened, waiting_until)),
    }


def task_times(snapshot: dict, now: datetime) -> dict[str, dict[str, int | None]]:
    pulls = _pulls_by_task(snapshot)
    return {task["item_id"]: _times(task, pulls[task["task"]], now) for task in snapshot["tasks"]}
