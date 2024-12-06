from calculator import Calculator

def test_integration():
    calc = Calculator()
    result = calc.solve(3, 2, '+')
    result = calc.solve(result, 2, '*')
    result = calc.solve(result, 2, '/')
    result = calc.solve(result, 1, '-')
    assert result == 4