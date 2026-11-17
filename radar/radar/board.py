from dataclasses import dataclass, field
from datetime import date, datetime
from zoneinfo import ZoneInfo

DONE = "Done"


@dataclass(frozen=True)
class Metric:
    semana: str
    etapa: str
    valor: float
    pessoa: str | None = None
    pessoa_id: str | None = field(default=None, compare=False)

    @property
    def title(self) -> str:
        title = f"{self.etapa} · {self.semana}"
        return f"{title} · {self.pessoa}" if self.pessoa else title


def days_in_status(since: str, today: date, timezone: str) -> int:
    changed = datetime.fromisoformat(since.replace("Z", "+00:00")).astimezone(ZoneInfo(timezone)).date()
    return (today - changed).days


def task_days(task: dict, today: date, timezone: str) -> int | None:
    if task["state"] != "OPEN" or not task["status"] or task["status"] == DONE or not task["status_since"]:
        return None
    return days_in_status(task["status_since"], today, timezone)


def plan_days(tasks: list[dict], current: dict[str, float], today: date, timezone: str) -> dict[str, int | None]:
    plan = {}
    for task in tasks:
        days = task_days(task, today, timezone)
        if current.get(task["item_id"]) != days:
            plan[task["item_id"]] = days
    return plan


def plan_metrics(existing: list[dict], metrics: list[Metric]) -> tuple[list[Metric], list[tuple[str, Metric]]]:
    on_board = {(item["semana"], item["etapa"], item.get("pessoa")): item for item in existing}
    creates, updates = [], []
    for metric in metrics:
        item = on_board.get((metric.semana, metric.etapa, metric.pessoa))
        if not item:
            creates.append(metric)
        elif item["valor"] != metric.valor:
            updates.append((item["item_id"], metric))
    return creates, updates


def plan_times(times: dict[str, dict], current: dict[str, dict]) -> list[tuple[str, str, int | None]]:
    plan = []
    for item_id, fields in times.items():
        for field, value in fields.items():
            if current.get(item_id, {}).get(field) != value:
                plan.append((item_id, field, value))
    return plan


def known_options(writes: list[tuple], options: dict[str, str]) -> list[tuple]:
    return [write for write in writes if write[2] is None or write[2] in options]


def known_weeks(metrics: list[Metric], options: dict[str, str]) -> tuple[list[Metric], list[str]]:
    kept = [metric for metric in metrics if metric.semana in options]
    skipped = sorted({metric.semana for metric in metrics if metric.semana not in options})
    return kept, skipped


SET_VALUE = """
mutation($project: ID!, $item: ID!, $field: ID!, $value: ProjectV2FieldValue!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field, value: $value}) {
    projectV2Item { id }
  }
}
"""

CLEAR_VALUE = """
mutation($project: ID!, $item: ID!, $field: ID!) {
  clearProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field}) {
    projectV2Item { id }
  }
}
"""

ADD_DRAFT = """
mutation($project: ID!, $title: String!, $assignees: [ID!]) {
  addProjectV2DraftIssue(input: {projectId: $project, title: $title, assigneeIds: $assignees}) { projectItem { id } }
}
"""


class Board:
    def __init__(self, client, project_id: str, fields: dict):
        self.client = client
        self.project_id = project_id
        self.fields = fields

    def _set(self, item_id: str, name: str, value: dict):
        self.client.graphql(SET_VALUE, project=self.project_id, item=item_id, field=self.fields[name]["id"], value=value)

    def _option(self, name: str, option: str) -> dict:
        return {"singleSelectOptionId": self.fields[name]["options"][option]}

    def set_number(self, item_id: str, field: str, value: int | None):
        if value is None:
            self.client.graphql(CLEAR_VALUE, project=self.project_id, item=item_id, field=self.fields[field]["id"])
        else:
            self._set(item_id, field, {"number": value})

    def set_option(self, item_id: str, field: str, option: str | None):
        if option is None:
            self.client.graphql(CLEAR_VALUE, project=self.project_id, item=item_id, field=self.fields[field]["id"])
        else:
            self._set(item_id, field, self._option(field, option))

    def set_days(self, item_id: str, days: int | None):
        self.set_number(item_id, "Dias no status", days)

    def create_metric(self, metric: Metric):
        assignees = [metric.pessoa_id] if metric.pessoa_id else []
        result = self.client.graphql(ADD_DRAFT, project=self.project_id, title=metric.title, assignees=assignees)
        item_id = result["addProjectV2DraftIssue"]["projectItem"]["id"]
        self._set(item_id, "Radar", self._option("Radar", "Métrica"))
        self._set(item_id, "Semana", self._option("Semana", metric.semana))
        self._set(item_id, "Etapa", self._option("Etapa", metric.etapa))
        self._set(item_id, "Valor", {"number": metric.valor})

    def update_metric(self, item_id: str, metric: Metric):
        self._set(item_id, "Valor", {"number": metric.valor})
