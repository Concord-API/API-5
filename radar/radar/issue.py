FIND = """
query($search: String!) {
  search(query: $search, type: ISSUE, first: 10) {
    nodes { ... on Issue { id title state comments(last: 1) { nodes { body } } } }
  }
}
"""

IDS = """
query($owner: String!, $repo: String!, $login: String!) {
  repository(owner: $owner, name: $repo) { id }
  user(login: $login) { id }
}
"""

CREATE = """
mutation($repo: ID!, $title: String!, $body: String!, $assignees: [ID!]) {
  createIssue(input: {repositoryId: $repo, title: $title, body: $body, assigneeIds: $assignees}) { issue { id } }
}
"""

COMMENT = """
mutation($subject: ID!, $body: String!) {
  addComment(input: {subjectId: $subject, body: $body}) { clientMutationId }
}
"""

INTRO = """Todo dia útil às 9h o Radar comenta aqui quem está travando a sprint:

- quem tem task aberta no nome e está há 2 dias úteis ou mais sem commit em nenhum repositório, sem comentar nas suas tasks e sem mover os seus cards;
- a partir de 4 dias úteis, o master é mencionado junto;
- para o master: tasks sem responsável, US sem nenhuma task e, quando a sprint tem US, pessoas sem task.

Fechar esta issue pausa as cobranças. Reabrir volta."""


class Tracker:
    def __init__(self, client, owner: str, repo: str, title: str):
        self.client = client
        self.owner = owner
        self.repo = repo
        self.title = title

    def find(self) -> dict | None:
        query = f'repo:{self.owner}/{self.repo} is:issue in:title "{self.title}"'
        for node in self.client.graphql(FIND, search=query)["search"]["nodes"]:
            if node.get("title") == self.title:
                comments = node["comments"]["nodes"]
                return {"id": node["id"], "state": node["state"], "last_comment": comments[0]["body"] if comments else None}
        return None

    def create(self, master: str) -> str:
        ids = self.client.graphql(IDS, owner=self.owner, repo=self.repo, login=master)
        result = self.client.graphql(CREATE, repo=ids["repository"]["id"], title=self.title, body=INTRO,
                                     assignees=[ids["user"]["id"]])
        return result["createIssue"]["issue"]["id"]

    def comment(self, issue_id: str, body: str):
        self.client.graphql(COMMENT, subject=issue_id, body=body)
