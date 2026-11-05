from runpy import run_path

gcd = run_path("code/40_gcd.py")["gcd"]


def test_gcd():
    assert gcd(12, 18) == 6


def test_coprime_numbers():
    assert gcd(7, 9) == 1


def test_same_numbers():
    assert gcd(10, 10) == 10


def test_zero():
    assert gcd(0, 5) == 5