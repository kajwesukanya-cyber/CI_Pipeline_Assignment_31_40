from runpy import run_path

remove_duplicates = run_path(
    "code/34_remove_duplicates.py"
)["remove_duplicates"]


def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]


def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]


def test_empty_list():
    assert remove_duplicates([]) == []


def test_all_same():
    assert remove_duplicates([5, 5, 5]) == [5]
    