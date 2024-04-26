from world import *

import pytest

from your_code_file import welcome, fibonacci_of, calculate_mean, binary_search


def test_welcome():
    assert welcome() == "Hello, World!"


def test_fibonacci():
    assert fibonacci_of(0) == 0
    assert fibonacci_of(1) == 1
    assert fibonacci_of(10) == 55


def test_calculate_mean():
    assert calculate_mean([1, 2, 3, 4, 5]) == 3.0


def test_binary_search():
    assert binary_search([1, 2, 3, 4, 5], 4) == 3
    assert binary_search([1, 2, 3, 4, 5], 1) == 0
    assert binary_search([1, 2, 3, 4, 5], 5) == 4
