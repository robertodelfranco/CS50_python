from fuel import convert, gauge
import pytest


def test_correct_input():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge_input():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

