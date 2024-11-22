from bank import value


def test_upper():
    assert value("HEllO, HOW ARE YOU??") == 0
    assert value("HELLO") == 0
    assert value("HOLA!!") == 20
    assert value("20 HOLA!!") == 100


def test_lower():
    assert value("hello, I'm okay!") == 0
    assert value("hola!!") == 20
    assert value("ola!!") == 100


def test_number():
    assert value("h2900") == 20
    assert value("2hola!!") == 100
    assert value("2HELLO") == 100

