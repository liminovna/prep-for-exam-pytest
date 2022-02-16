from src.t_project import DomainError, asin_degrees, acos_degrees, atan_degrees
import pytest

def test_arcsin():
    assert asin_degrees(0.5) == 30.0
    assert asin_degrees(1) == 90.0
    assert asin_degrees(0.7, 2) == 44.43
    assert asin_degrees(0.7, all_dec=True) == 44.4270040008057
    assert asin_degrees(0.7, 6) == 44.427004
    with pytest.raises(DomainError):
        asin_degrees(1.01)


def test_arccos():
    assert acos_degrees(0.5) == 60.0
    assert acos_degrees(1) == 0.0
    assert acos_degrees(0.7, 2) == 45.57
    assert acos_degrees(0.7, all_dec=True) == 45.5729959991943
    assert acos_degrees(0.7, 6) == 45.572996
    with pytest.raises(DomainError):
        acos_degrees(1.01)

def test_arctan():
    assert atan_degrees(0.5) == 26.565
    assert atan_degrees(1) == 45.0
    assert atan_degrees(0.7, 2) == 34.99
    assert atan_degrees(0.7, all_dec=True) == 34.99202019855866
    assert atan_degrees(0.7, 6) == 34.992020
    assert atan_degrees(1.1) == 47.726