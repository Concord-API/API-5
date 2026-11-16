from dataclasses import dataclass
from datetime import date, datetime
from zoneinfo import ZoneInfo

DONE = "Done"


@dataclass(frozen=True)
class Metric:
    semana: str
    etapa: str
    valor: float

    @property
    def title(self) -> str:
        return f"{self.etapa} · {self.semana}"


def days_in_status(since: str, today: date, timezone: str) -> int:
    changed = datetime.fromisoformat(since.replace("Z", "+00:00")).astimezone(ZoneInfo(timezone)).date()
    return (today - changed).days


def plan_days(tasks: list[dict], current: dict[str, float], today: date, timezone: str) -> dict[str, int]:
    plan = {}
    for task in tasks:
        if task["state"] != "OPEN" or not task["status"] or task["status"] == DONE or not task["status_since"]:
            continue
        days = days_in_status(task["status_since"], today, timezone)
        if current.get(task["item_id"]) != days:
            plan[task["item_id"]] = days
    return plan


def plan_metrics(existing: list[dict], metrics: list[Metric]) -> tuple[list[Metric], list[tuple[str, Metric]]]:
    on_board = {(item["semana"], item["etapa"]): item for item in existing}
    creates, updates = [], []
    for metric in metrics:
        item = on_board.get((metric.semana, metric.etapa))
        if not item:
            creates.append(metric)
        elif item["valor"] != metric.valor:
            updates.append((item["item_id"], metric))
    return creates, updates


SET_VALUE = """
mutation($project: ID!, $item: ID!, $field: ID!, $value: ProjectV2FieldValue!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field, value: $value}) {
    projectV2Item { id }
  }
}
"""

ADD_DRAFT = """
mutation($project: ID!, $title: String!) {
  addProjectV2DraftIssue(input: {projectId: $project, title: $title}) { projectItem { id } }
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

    def set_days(self, item_id: str, days: int):
        self._set(item_id, "Dias no status", {"number": days})

    def create_metric(self, metric: Metric):
        result = self.client.graphql(ADD_DRAFT, project=self.project_id, title=metric.title)
        item_id = result["addProjectV2DraftIssue"]["projectItem"]["id"]
        self._set(item_id, "Radar", self._option("Radar", "Métrica"))
        self._set(item_id, "Semana", {"text": metric.semana})
        self._set(item_id, "Etapa", self._option("Etapa", metric.etapa))
        self._set(item_id, "Valor", {"number": metric.valor})

    def update_metric(self, item_id: str, metric: Metric):
        self._set(item_id, "Valor", {"number": metric.valor})
