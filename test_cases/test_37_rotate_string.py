from runpy import run_path

rotate_string = run_path(
    "code/37_rotate_string.py"
)["rotate_string"]


def test_rotate_string():
    assert rotate_string("abcdef", 2) == "cdefab"


def test_rotate_zero_positions():
    assert rotate_string("python", 0) == "python"


def test_rotate_full_length():
    assert rotate_string("hello", 5) == "hello"


def test_empty_string():
    assert rotate_string("", 2) == ""