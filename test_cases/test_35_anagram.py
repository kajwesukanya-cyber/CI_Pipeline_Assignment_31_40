from runpy import run_path

is_anagram = run_path("code/35_anagram.py")["is_anagram"]


def test_valid_anagram():
    assert is_anagram("listen", "silent")


def test_invalid_anagram():
    assert not is_anagram("hello", "world")


def test_uppercase_anagram():
    assert is_anagram("Listen", "Silent")


def test_same_word():
    assert is_anagram("python", "python")