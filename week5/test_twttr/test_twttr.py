from twttr import shorten


def test_upper():
    assert shorten("HELLO") == "HLL"
    assert shorten("CS50 IS FUN!!") == "CS50 S FN!!"


def test_lower():
    assert shorten("house:1") == "hs:1"
    assert shorten("hello, world! 123") == "hll, wrld! 123"

