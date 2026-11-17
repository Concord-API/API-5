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
COMMITS_BY_PERSON = "Commits por pessoa"
BEFORE_START = "Antes do início"
AFTER_END = "Depois do fim"


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
        return {FIRST_COMMIT: _rounded(waiting)}
    first_commit = min(_instant(p["first_commit_at"] or p["created_at"]) for p in pulls)
    return {FIRST_COMMIT: _rounded(_days(created, first_commit))}


def task_times(snapshot: dict, now: datetime) -> dict[str, dict[str, int | None]]:
    pulls = _pulls_by_task(snapshot)
    return {task["item_id"]: _times(task, pulls[task["task"]], now) for task in snapshot["tasks"]}


def _sprint_of_day(day: date, sprints: list[Sprint]) -> Sprint | None:
    for sprint in sprints:
        if day <= sprint.end:
            return sprint
    return None


def created_in(task: dict, sprints: list[Sprint], timezone: str) -> str | None:
    created = _local_day(task["created_at"], timezone)
    by_number = {sprint.number: sprint for sprint in sprints}
    sprint = by_number.get(task["sprint"]) if task.get("sprint") else _sprint_of_day(created, sprints)
    if sprint is None:
        return None
    if created < sprint.start:
        return BEFORE_START
    if created > sprint.end:
        return AFTER_END
    return f"Semana {min(3, (created - sprint.start).days // 7 + 1)}"


def person_metrics(snapshot: dict, sprints: list[Sprint], today: date, timezone: str) -> list[Metric]:
    counts = Counter()
    ids = {}
    for commit in snapshot["commits"]:
        if not commit.get("author"):
            continue
        day = _local_day(commit["date"], timezone)
        sprint = next((s for s in sprints if s.start - WEEK <= day <= s.end), None)
        if sprint is None or sprint.start - WEEK > today:
            continue
        counts[(sprint.number, commit["author"])] += 1
        ids[commit["author"]] = commit["author_id"]
    return [
        Metric(f"S{number}", COMMITS_BY_PERSON, total, person, ids[person])
        for (number, person), total in sorted(counts.items())
    ]
