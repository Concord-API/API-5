import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

from radar import fetch
from radar.board import Board, known_options, known_weeks, plan_days, plan_metrics, plan_times, task_days
from radar.collect import build_snapshot
from radar.github import GitHub
from radar.links import story_label
from radar.metrics import FIRST_COMMIT, created_in, person_metrics, task_times, week_metrics
from radar.sprints import read_sprints


def run(client: GitHub, config: dict, root: Path, out: Path, dry_run: bool) -> dict:
    timezone = config["timezone"]
    now = datetime.now(ZoneInfo(timezone))
    today = now.date()
    owner, number = config["owner"], config["project"]

    sprints = read_sprints(root, config["sprint_backlogs"])
    project = fetch.project(client, owner, number)
    items = fetch.items(client, owner, number)
    pulls = {repo: fetch.pulls(client, owner, repo) for repo in config["code_repos"]}

    snapshot = build_snapshot(today, sprints, items, pulls)
    for task in snapshot["tasks"]:
        task["days_in_status"] = task_days(task, today, timezone)

    current = {item["id"]: item["dias"]["number"] for item in items if item["dias"]}
    days = plan_days(snapshot["tasks"], current, today, timezone)
    metrics = week_metrics(snapshot, sprints, today, timezone) + person_metrics(snapshot, sprints, today, timezone)
    times = task_times(snapshot, now)
    for task in snapshot["tasks"]:
        task["times"] = times[task["item_id"]]
    aliases = {FIRST_COMMIT: "firstCommit"}
    current_times = {
        item["id"]: {field: (item.get(alias) or {}).get("number") for field, alias in aliases.items()}
        for item in items
    }
    time_writes = plan_times(times, current_times)
    stories = {
        task["item_id"]: {"US": story_label(task["task"]), "Criada": created_in(task, sprints, timezone)}
        for task in snapshot["tasks"]
    }
    current_stories = {
        item["id"]: {"US": (item.get("us") or {}).get("name"), "Criada": (item.get("criada") or {}).get("name")}
        for item in items
    }
    story_writes = [
        write for write in plan_times(stories, current_stories)
        if known_options([write], project["fields"].get(write[1], {}).get("options", {}))
    ]
    snapshot["computed"] = [{"semana": m.semana, "etapa": m.etapa, "valor": m.valor} for m in metrics]
    week_options = project["fields"].get("Semana", {}).get("options", {})
    metrics, skipped_weeks = known_weeks(metrics, week_options)
    creates, updates = plan_metrics(snapshot["metrics"], metrics)

    out.mkdir(parents=True, exist_ok=True)
    (out / f"{snapshot['date']}.json").write_text(json.dumps(snapshot, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    if not dry_run:
        board = Board(client, project["id"], project["fields"])
        for item_id, value in days.items():
            board.set_days(item_id, value)
        for item_id, field, value in time_writes:
            board.set_number(item_id, field, value)
        for item_id, field, value in story_writes:
            board.set_option(item_id, field, value)
        for metric in creates:
            board.create_metric(metric)
        for item_id, metric in updates:
            board.update_metric(item_id, metric)

    return {
        "date": snapshot["date"],
        "tasks": len(snapshot["tasks"]),
        "pulls": len(snapshot["pulls"]),
        "commits": len(snapshot["commits"]),
        "days_written": len(days),
        "times_written": len(time_writes),
        "stories_written": len(story_writes),
        "metrics_created": len(creates),
        "metrics_updated": len(updates),
        "weeks_without_option": skipped_weeks,
        "dry_run": dry_run,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(prog="radar")
    parser.add_argument("--config", default=".github/radar.yml")
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    config = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    summary = run(GitHub(os.environ["RADAR_TOKEN"]), config, Path(args.root), Path(args.out), args.dry_run)
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
