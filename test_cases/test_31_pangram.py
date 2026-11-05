def test_pangram():
    text = "The quick brown fox jumps over the lazy dog"
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    assert alphabet.issubset(set(text.lower()))


def test_not_pangram():
    text = "Hello World"
    alphabet = set("abcdefghijklmnopqrstuvwxyz")

    assert not alphabet.issubset(set(text.lower()))
