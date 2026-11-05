def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    return alphabet.issubset(set(text.lower()))    