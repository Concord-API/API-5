import json
import urllib.request

GRAPHQL = "https://api.github.com/graphql"


class GitHub:
    def __init__(self, token: str, url: str = GRAPHQL):
        self.token = token
        self.url = url

    def _post(self, body: dict) -> dict:
        request = urllib.request.Request(
            self.url,
            data=json.dumps(body).encode("utf-8"),
            headers={
                "Authorization": f"bearer {self.token}",
                "Content-Type": "application/json",
                "User-Agent": "concord-radar",
            },
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            return json.load(response)

    def graphql(self, query: str, **variables) -> dict:
        payload = self._post({"query": query, "variables": variables})
        if payload.get("errors"):
            raise RuntimeError(json.dumps(payload["errors"], ensure_ascii=False))
        return payload["data"]

    def paginate(self, query: str, path: tuple[str, ...], **variables):
        cursor = None
        while True:
            connection = self.graphql(query, cursor=cursor, **variables)
            for key in path:
                connection = connection[key]
            yield from connection["nodes"]
            if not connection["pageInfo"]["hasNextPage"]:
                return
            cursor = connection["pageInfo"]["endCursor"]
