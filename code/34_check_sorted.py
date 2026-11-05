from runpy import run_path

is_sorted = run_path(
    "code/34_check_sorted.py"
)["is_sorted"]


def test_sorted_list():
    assert is_sorted([1, 2, 3, 4, 5]) == True


def test_unsorted_list():
    assert is_sorted([5, 3, 2, 1]) == False


def test_empty_list():
    assert is_sorted([]) == True


def test_single_element():
    assert is_sorted([10]) == True
    