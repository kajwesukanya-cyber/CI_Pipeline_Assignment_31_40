from runpy import run_path

move_zeros = run_path(
    "code/35_move_zeros.py"
)["move_zeros"]


def test_move_zeros():
    assert move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_no_zeros():
    assert move_zeros([1, 2, 3]) == [1, 2, 3]


def test_all_zeros():
    assert move_zeros([0, 0, 0]) == [0, 0, 0]


def test_empty_list():
    assert move_zeros([]) == []
    