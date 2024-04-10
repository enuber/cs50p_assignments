from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(24)
    assert jar.capacity == 24
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(6)
    assert jar.size == 6


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    jar.withdraw(4)
    assert jar.size == 4

    jar.withdraw(4)
    assert jar.size == 0
