from app import add, divide, multiply


def test_add():
    assert add(2, 3) == 5


def test_multiply() -> None:
    assert multiply(5, 10) == 50


def test_divide() -> None:
    assert divide(10, 5) == 2
