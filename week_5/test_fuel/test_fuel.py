from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("1/10") == 10

def test_convert_exceptions():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")
        convert("20/0")
    with pytest.raises(ValueError):
        convert("2/1")
        convert("20/10")
        convert("3/2")
        convert("4/3")

def test_gauge():
    assert gauge(10) == "10%"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"