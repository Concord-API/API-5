from radar.fetch import branch_commits


class Pages:
    def __init__(self, pages):
        self.pages = list(pages)

    def paginate(self, query, path, **variables):
        return iter(self.pages)


def ref(*commits):
    return {"target": {"history": {"nodes": [
        {"authoredDate": at, "author": {"user": {"login": login} if login else None}} for at, login in commits]}}}


def test_reads_the_recent_commits_of_every_branch_even_without_a_pull_request():
    client = Pages([ref(("2026-12-02T12:00:00Z", "ana"), ("2026-12-01T12:00:00Z", None)), {"target": None}])

    assert branch_commits(client, "Concord-API", "API5-Backend", "2026-11-23T00:00:00Z") == [
        {"date": "2026-12-02T12:00:00Z", "author": "ana"}]
