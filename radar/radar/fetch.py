from radar.github import GitHub

PROJECT = """
query($owner: String!, $number: Int!) {
  organization(login: $owner) {
    projectV2(number: $number) {
      id
      fields(first: 50) {
        nodes {
          ... on ProjectV2FieldCommon { id name }
          ... on ProjectV2SingleSelectField { options { id name } }
        }
      }
    }
  }
}
"""

ITEMS = """
query($owner: String!, $number: Int!, $cursor: String) {
  organization(login: $owner) {
    projectV2(number: $number) {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          type
          content {
            ... on Issue {
              number title state createdAt closedAt
              assignees(first: 10) { nodes { login } }
            }
            ... on DraftIssue { title }
          }
          status: fieldValueByName(name: "Status") {
            ... on ProjectV2ItemFieldSingleSelectValue { name updatedAt }
          }
          radar: fieldValueByName(name: "Radar") {
            ... on ProjectV2ItemFieldSingleSelectValue { name }
          }
          semana: fieldValueByName(name: "Semana") {
            ... on ProjectV2ItemFieldSingleSelectValue { name }
          }
          etapa: fieldValueByName(name: "Etapa") {
            ... on ProjectV2ItemFieldSingleSelectValue { name }
          }
          valor: fieldValueByName(name: "Valor") {
            ... on ProjectV2ItemFieldNumberValue { number }
          }
          dias: fieldValueByName(name: "Dias no status") {
            ... on ProjectV2ItemFieldNumberValue { number }
          }
        }
      }
    }
  }
}
"""

PULLS = """
query($owner: String!, $repo: String!, $cursor: String) {
  repository(owner: $owner, name: $repo) {
    pullRequests(first: 25, after: $cursor, orderBy: {field: CREATED_AT, direction: ASC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number headRefName baseRefName createdAt mergedAt
        reviews(first: 20) { nodes { submittedAt } }
        commits(first: 100) {
          pageInfo { hasNextPage endCursor }
          nodes { commit { oid authoredDate parents { totalCount } } }
        }
      }
    }
  }
}
"""

PULL_COMMITS = """
query($owner: String!, $repo: String!, $number: Int!, $cursor: String) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      commits(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes { commit { oid authoredDate parents { totalCount } } }
      }
    }
  }
}
"""


def fields_by_name(nodes: list[dict]) -> dict:
    return {
        node["name"]: {"id": node["id"], "options": {o["name"]: o["id"] for o in node.get("options", [])}}
        for node in nodes
        if node.get("name")
    }


def project(client: GitHub, owner: str, number: int) -> dict:
    data = client.graphql(PROJECT, owner=owner, number=number)["organization"]["projectV2"]
    return {"id": data["id"], "fields": fields_by_name(data["fields"]["nodes"])}


def items(client: GitHub, owner: str, number: int) -> list[dict]:
    nodes = client.paginate(ITEMS, ("organization", "projectV2", "items"), owner=owner, number=number)
    return [node for node in nodes if node["content"]]


def pulls(client: GitHub, owner: str, repo: str) -> list[dict]:
    result = []
    for pull in client.paginate(PULLS, ("repository", "pullRequests"), owner=owner, repo=repo):
        if pull["commits"]["pageInfo"]["hasNextPage"]:
            pull["commits"]["nodes"] = list(client.paginate(
                PULL_COMMITS, ("repository", "pullRequest", "commits"), owner=owner, repo=repo, number=pull["number"]))
        result.append(pull)
    return result
