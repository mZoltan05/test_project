import pytest
from calculator import Calculator

def test_addition():
    calc = Calculator()
    assert calc.solve(3, 2, '+') == 5

def test_subtraction():
    calc = Calculator()
    assert calc.solve(3, 2, '-') == 1

def test_multiplication():
    calc = Calculator()
    assert calc.solve(3, 2, '*') == 6

def test_division():
    calc = Calculator()
    assert calc.solve(6, 2, '/') == 3

def test_division_by_zero():
    calc = Calculator()
    with pytest.raises(ValueError, match="Can't divide by zero!"):
        calc.solve(6, 0, '/')

def test_invalid_operator():
    calc = Calculator()
    with pytest.raises(ValueError, match="Invalid operator"):
        calc.solve(6, 2, '%')

def test_integration():
    calc = Calculator()
    result = calc.solve(3, 2, '+')
    result = calc.solve(result, 2, '*')
    result = calc.solve(result, 2, '/')
    result = calc.solve(result, 1, '-')
    assert result == 4