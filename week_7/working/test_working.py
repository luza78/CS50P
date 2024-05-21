from working import convert
import pytest


def main():
    test_1()
    test_2()
    test_3()


def test_1():
    assert convert("5 AM to 7 PM") == "05:00 to 19:00"
    assert convert("12 AM to 12:30 PM") == "00:00 to 12:30"
    assert convert("12:59 AM to 1:39 PM") == "00:59 to 13:39"


def test_2():
    assert convert("4 AM to 10 PM") == "04:00 to 22:00"
    assert convert("11 AM to 11 PM") == "11:00 to 23:00"
    assert convert("12:11 AM to 2 PM") == "00:11 to 14:00"


def test_3():
    with pytest.raises(ValueError):
        convert("5 AM 7 PM")
    with pytest.raises(ValueError):
        convert("5 to 7 PM")
    with pytest.raises(ValueError):
        convert("5 AM to 7")
    with pytest.raises(ValueError):
        convert("5 to 7")
    with pytest.raises(ValueError):
        convert("5:61 AM to 12 PM")
    with pytest.raises(ValueError):
        convert("9:61 PM to 4 PM")


if __name__ == "__main__":
    main()
