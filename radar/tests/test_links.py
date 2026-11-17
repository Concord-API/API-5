import pytest

from radar.links import story_label, story_of, task_from_branch, task_from_title


@pytest.mark.parametrize("title, task", [
    ("27.3 Add the CSV export endpoint", "27.3"),
    ("0.85 Analyze the pipeline quality and coverage with SonarQube Cloud", "0.85"),
    ("DVP-59 Collect the k6 results", "DVP-59"),
    ("US-27 — As a user, I want to export to CSV", None),
    ("DevOps", None),
])
def test_finds_the_task_in_the_issue_title(title, task):
    assert task_from_title(title) == task


@pytest.mark.parametrize("branch, task", [
    ("27.3-Add-the-CSV-export-endpoint", "27.3"),
    ("0.111-Make-the-panel-pages-stand-out", "0.111"),
    ("DVP-59-Collect-the-k6-results", "DVP-59"),
    ("us27", None),
    ("main", None),
    ("RATIO-DOCS-README.md", None),
])
def test_finds_the_task_in_the_branch_name(branch, task):
    assert task_from_branch(branch) == task


@pytest.mark.parametrize("task, story", [
    ("27.3", "US-27"),
    ("2.6", "US-02"),
    ("0.85", "US-00"),
    ("DVP-59", None),
])
def test_a_task_belongs_to_the_story_of_its_number(task, story):
    assert story_of(task) == story


@pytest.mark.parametrize("task, label", [
    ("27.3", "US-27"),
    ("2.6", "US-02"),
    ("0.85", "Foundation"),
    ("DVP-59", "DevOps"),
])
def test_names_the_story_of_a_task_for_the_board(task, label):
    assert story_label(task) == label
