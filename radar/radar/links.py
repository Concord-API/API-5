import re

TASK = r"(\d+\.\d+|DVP-\d+)"
TITLE = re.compile(rf"^{TASK}\s")
BRANCH = re.compile(rf"^{TASK}-")
STORY = re.compile(r"^(\d+)\.\d+$")


def task_from_title(title: str) -> str | None:
    match = TITLE.match(title)
    return match.group(1) if match else None


def task_from_branch(branch: str) -> str | None:
    match = BRANCH.match(branch)
    return match.group(1) if match else None


def story_of(task: str) -> str | None:
    match = STORY.match(task)
    return f"US-{int(match.group(1)):02d}" if match else None
