import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

WINDOW = re.compile(r"\*\*Window:\*\*\s*([A-Z][a-z]{2}) (\d{1,2}) to ([A-Z][a-z]{2}) (\d{1,2}), (\d{4})")
FOLDER_NUMBER = re.compile(r"(\d+)")
MONTHS = {name: number for number, name in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], start=1)}


@dataclass(frozen=True)
class Sprint:
    number: int
    start: date
    end: date


def parse_window(text: str, number: int) -> Sprint | None:
    match = WINDOW.search(text)
    if not match:
        return None
    start_month, start_day, end_month, end_day, year = match.groups()
    end = date(int(year), MONTHS[end_month], int(end_day))
    start_year = end.year - 1 if MONTHS[start_month] > end.month else end.year
    start = date(start_year, MONTHS[start_month], int(start_day))
    return Sprint(number, start, end)


def read_sprints(root: Path, pattern: str) -> list[Sprint]:
    sprints = []
    for path in root.glob(pattern):
        number = FOLDER_NUMBER.search(path.parent.name)
        if not number:
            continue
        sprint = parse_window(path.read_text(encoding="utf-8"), int(number.group(1)))
        if sprint:
            sprints.append(sprint)
    return sorted(sprints, key=lambda sprint: sprint.number)


def sprint_of(day: date | datetime, sprints: list[Sprint]) -> int | None:
    if isinstance(day, datetime):
        day = day.date()
    for sprint in sprints:
        if sprint.start <= day <= sprint.end:
            return sprint.number
    return None
