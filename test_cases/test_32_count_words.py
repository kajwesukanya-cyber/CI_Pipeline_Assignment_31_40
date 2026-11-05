from runpy import run_path

count_words = run_path("code/32_count_words.py")["count_words"]


def test_count_words():
    assert count_words("Hello how are you") == 4


def test_single_word():
    assert count_words("Python") == 1


def test_empty_string():
    assert count_words("") == 0


def test_multiple_spaces():
    assert count_words("Hello   World") == 2
    