from dataclasses import dataclass, field
from datetime import date, timedelta

from radar.metrics import _local_day
from radar.sprints import Sprint

DONE = "Done"
WEEKEND = (5, 6)


@dataclass(frozen=True)
class Rules:
    master: str
    team: list[str]
    no_task_expected: list[str] = field(default_factory=list)
    idle_days: int = 2
    escalate_days: int = 4


def business_days(since: date, today: date) -> int:
    days, day = 0, since + timedelta(days=1)
    while day <= today:
        if day.weekday() not in WEEKEND:
            days += 1
        day += timedelta(days=1)
    return days


def current_sprint(sprints: list[Sprint], today: date) -> Sprint | None:
    return next((sprint for sprint in sprints if sprint.start <= today <= sprint.end), None)


def last_commits(commits: list[dict], timezone: str) -> dict[str, date]:
    last = {}
    for commit in commits:
        if commit.get("author"):
            day = _local_day(commit["date"], timezone)
            last[commit["author"]] = max(day, last.get(commit["author"], day))
    return last


def _open_in(task: dict, sprint: Sprint) -> bool:
    return task["sprint"] == sprint.number and task["state"] == "OPEN" and task["status"] != DONE


def plan_alerts(snapshot: dict, sprint: Sprint, today: date, rules: Rules, commits: dict[str, date]) -> dict:
    tasks = [task for task in snapshot["tasks"] if _open_in(task, sprint)]
    in_sprint = [story for story in snapshot["stories"] if story["sprint"] == sprint.number]
    idle, without_task = [], []
    for login in rules.team:
        mine = sorted(task["number"] for task in tasks if login in task["assignees"])
        if not mine:
            if in_sprint and login not in rules.no_task_expected:
                without_task.append(login)
            continue
        days = business_days(max(commits.get(login, sprint.start), sprint.start), today)
        if days >= rules.idle_days:
            idle.append({"login": login, "days": days, "tasks": mine, "escalate": days >= rules.escalate_days})
    with_tasks = {task["story"] for task in snapshot["tasks"]}
    stories = [
        story["story"] for story in in_sprint if story["state"] == "OPEN" and story["story"] not in with_tasks
    ]
    return {
        "idle": idle,
        "unassigned": sorted(task["number"] for task in tasks if not task["assignees"]),
        "without_task": without_task,
        "stories_without_tasks": sorted(stories),
    }


def marker(today: date) -> str:
    return f"<!-- radar:{today.isoformat()} -->"


def _plural(count: int, word: str) -> str:
    return f"{count} {word}" if count == 1 else f"{count} {word}s"


def _numbers(numbers: list[int]) -> str:
    return ", ".join(f"#{number}" for number in numbers)


def render(alerts: dict, sprint: Sprint, today: date, rules: Rules) -> str:
    lines = [marker(today), f"### 🚨 Travas de {today:%d/%m} · Sprint {sprint.number}", ""]
    if alerts["idle"]:
        lines += ["**Parados com task no nome**"]
        for person in alerts["idle"]:
            icon = "🔥" if person["escalate"] else "⏰"
            line = (f"- {icon} @{person['login']}, **{person['days']} dias úteis** sem commit, comentário ou card movido, com "
                    f"{_plural(len(person['tasks']), 'task')} no nome: {_numbers(person['tasks'])}")
            escalate = person["escalate"] and person["login"] != rules.master
            lines.append(line + (f" · @{rules.master}" if escalate else ""))
        lines.append("")
    master = []
    if alerts["unassigned"]:
        count = len(alerts["unassigned"])
        master.append(f"- 📌 {_plural(count, 'task')} sem ninguém: {_numbers(alerts['unassigned'])}")
    if alerts["without_task"]:
        master.append("- 🙋 Sem task na sprint: " + ", ".join(f"`{login}`" for login in alerts["without_task"]))
    if alerts["stories_without_tasks"]:
        master.append("- 📝 US sem nenhuma task: " + ", ".join(alerts["stories_without_tasks"]))
    if master:
        lines += [f"**Para o @{rules.master}**", *master, ""]
    if not alerts["idle"] and not master:
        lines += ["✅ Nenhuma trava hoje.", ""]
    lines.append("_Fechar esta issue pausa as cobranças. Reabrir volta._")
    return "\n".join(lines)


def next_step(issue: dict | None, today_marker: str) -> str:
    if issue is None:
        return "create"
    if issue["state"] != "OPEN":
        return "paused"
    if (issue["last_comment"] or "").startswith(today_marker):
        return "already"
    return "comment"
