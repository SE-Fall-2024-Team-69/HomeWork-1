import pytest

from myfile import find_number

# for testing
# def test_find_number_fail():
#     number = find_number()
#     assert number == (1, 12, 9, 1)

def test_find_number_pass():
    number = find_number()
    assert number == (1, 12, 9, 10)


    