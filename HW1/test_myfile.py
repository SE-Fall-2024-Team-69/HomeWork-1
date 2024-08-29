import pytest

from myfile import find_number

# Test that will fail
def test_find_number():
    number = find_number()
    assert number == (1, 12, 9, 1)

# Test that will pass
def test_find_number():
    number = find_number()
    assert number == (1, 12, 9, 10)
