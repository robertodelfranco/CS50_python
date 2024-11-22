from plates import is_valid


def test_begging():
    assert is_valid("AA50") == True
    assert is_valid("A50") == False


def test_length():
    assert is_valid("HELLO") == True
    assert is_valid("HELLO, WORLD") == False
    assert is_valid("GOODBYE") == False


def test_number():
    assert is_valid("9X") == False
    assert is_valid("AA5X89") == False


def test_alphanumeric():
    assert is_valid("AA50") == True
    assert is_valid("AA!!!") == False


def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("0") == False
    assert is_valid("AA0567") == False

