from datetime import date

from radar.sprints import Sprint, parse_window, read_sprints, sprint_of


def test_reads_the_window_of_a_sprint_backlog():
    text = "# Sprint Backlog — Sprint 3\n\n**Window:** Nov 2 to Nov 22, 2026\n"

    assert parse_window(text, 3) == Sprint(3, date(2026, 11, 2), date(2026, 11, 22))


def test_a_window_that_crosses_the_year_starts_in_the_previous_year():
    text = "**Window:** Dec 28 to Jan 17, 2027"

    assert parse_window(text, 7) == Sprint(7, date(2026, 12, 28), date(2027, 1, 17))


def test_a_backlog_without_window_is_ignored():
    assert parse_window("# Sprint Backlog — Sprint 4\n", 4) is None


def test_reads_every_sprint_folder_in_order(tmp_path):
    for number, window in [(2, "Oct 5 to Oct 25, 2026"), (1, "Sep 7 to Sep 27, 2026"), (10, "Feb 1 to Feb 21, 2027")]:
        folder = tmp_path / f"sprint{number}"
        folder.mkdir()
        (folder / "sprint-backlog.md").write_text(f"**Window:** {window}\n")
    (tmp_path / "sprint4").mkdir()
    (tmp_path / "sprint4" / "sprint-backlog.md").write_text("no window yet\n")

    sprints = read_sprints(tmp_path, "sprint*/sprint-backlog.md")

    assert [s.number for s in sprints] == [1, 2, 10]
    assert sprints[0].start == date(2026, 9, 7)


def test_a_day_belongs_to_the_sprint_whose_window_holds_it():
    sprints = [Sprint(1, date(2026, 9, 7), date(2026, 9, 27)), Sprint(2, date(2026, 10, 5), date(2026, 10, 25))]

    assert sprint_of(date(2026, 9, 27), sprints) == 1
    assert sprint_of(date(2026, 10, 5), sprints) == 2
    assert sprint_of(date(2026, 9, 30), sprints) is None
