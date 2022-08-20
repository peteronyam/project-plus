import pytest
from newm import square


def test_positives():
    assert square(2) == 4
    assert square(3) == 9


def test_negatives():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zeros():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("dog")


