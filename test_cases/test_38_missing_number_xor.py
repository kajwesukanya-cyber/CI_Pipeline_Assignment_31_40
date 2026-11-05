from runpy import run_path

find_missing_number = run_path(
    "code/38_missing_number_xor.py"
)["find_missing_number"]


def test_missing_middle_number():
    assert find_missing_number([1, 2, 4, 5]) == 3


def test_missing_first_number():
    assert find_missing_number([2, 3, 4, 5]) == 1


def test_missing_last_number():
    assert find_missing_number([1, 2, 3, 4]) == 5


def test_two_numbers():
    assert find_missing_number([1]) == 2
    