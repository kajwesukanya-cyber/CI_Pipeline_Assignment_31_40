import importlib.util
from pathlib import Path

file_path = Path(__file__).resolve().parents[1] / "code" / "31_pangram.py"

spec = importlib.util.spec_from_file_location("pangram", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def test_pangram():
    text = "The quick brown fox jumps over the lazy dog"
    assert module.is_pangram(text) == True


def test_not_pangram():
    text = "Hello World"
    assert module.is_pangram(text) == False


def test_empty_string():
    assert module.is_pangram("") == False


def test_uppercase():
    text = "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
    assert module.is_pangram(text) == True