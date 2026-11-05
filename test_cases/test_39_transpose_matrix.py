from runpy import run_path

transpose_matrix = run_path(
    "code/39_transpose_matrix.py"
)["transpose_matrix"]


def test_transpose_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_square_matrix():
    assert transpose_matrix([[1, 2], [3, 4]]) == [
        [1, 3],
        [2, 4]
    ]


def test_single_element():
    assert transpose_matrix([[5]]) == [[5]]


def test_empty_matrix():
    assert transpose_matrix([]) == []