from runpy import run_path

first_non_repeating = run_path(
    "code/33_first_non_repeating.py"
)["first_non_repeating"]


def test_first_non_repeating():
    assert first_non_repeating("swiss") == "w"


def test_first_character():
    assert first_non_repeating("hello") == "h"


def test_all_repeating():
    assert first_non_repeating("aabbcc") is None


def test_single_character():
    assert first_non_repeating("a") == "a"