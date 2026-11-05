from runpy import run_path

most_frequent = run_path(
    "code/36_most_frequent.py"
)["most_frequent"]


def test_most_frequent():
    assert most_frequent([1, 2, 3, 2, 4, 2, 5]) == 2


def test_single_element():
    assert most_frequent([10]) == 10


def test_all_same_elements():
    assert most_frequent([5, 5, 5]) == 5


def test_empty_list():
    assert most_frequent([]) == None
    