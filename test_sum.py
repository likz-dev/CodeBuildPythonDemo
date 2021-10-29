def sum(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def test_sum():
    assert sum(1, 2) == 3


def test_subtract():
    assert subtract(5, 4) == 1


def test_multiply():
    assert multiply(2, 3) == 6


def test_divide():
    assert divide(4, 2) == 2
