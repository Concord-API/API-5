import pytest

from radar.fetch import fields_by_name
from radar.github import GitHub


class Recorded(GitHub):
    def __init__(self, pages):
        super().__init__("token")
        self.pages = list(pages)
        self.cursors = []

    def graphql(self, query, **variables):
        self.cursors.append(variables.get("cursor"))
        return self.pages.pop(0)


def page(nodes, next_cursor=None):
    return {"repository": {"pullRequests": {
        "pageInfo": {"hasNextPage": next_cursor is not None, "endCursor": next_cursor},
        "nodes": nodes,
    }}}


def test_follows_the_cursor_until_the_last_page():
    client = Recorded([page([1, 2], "c1"), page([3], "c2"), page([4])])

    nodes = list(client.paginate("query", ("repository", "pullRequests")))

    assert nodes == [1, 2, 3, 4]
    assert client.cursors == [None, "c1", "c2"]


def test_raises_when_the_api_answers_with_errors(monkeypatch):
    client = GitHub("token")
    monkeypatch.setattr(client, "_post", lambda body: {"errors": [{"message": "Could not resolve"}]})

    with pytest.raises(RuntimeError, match="Could not resolve"):
        client.graphql("query")


def test_indexes_the_project_fields_and_options_by_name():
    nodes = [
        {"id": "F1", "name": "Status", "options": [{"id": "o1", "name": "Todo"}]},
        {"id": "F2", "name": "Valor"},
    ]

    assert fields_by_name(nodes) == {
        "Status": {"id": "F1", "options": {"Todo": "o1"}},
        "Valor": {"id": "F2", "options": {}},
    }
