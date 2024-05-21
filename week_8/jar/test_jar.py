from jar import Jar
import pytest


def main():
    ...


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪"


def test_deposit():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12
    jar.deposit(10)
    assert jar.size == 10
    with pytest.raises(ValueError):
        jar.deposit(3)
    with pytest.raises(ValueError):
        jar.deposit(20)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(ValueError):
        jar.withdraw(13)
    with pytest.raises(ValueError):
        jar.withdraw(99)


def test_size():
    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0
    jar.deposit(10)
    assert jar.size == 10


if __name__ == "__main__":
    main()
