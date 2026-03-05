from calculator_logic import calculate

def test_user_addition_flow():
    expression = "5+3"
    result = calculate(expression)
    assert result == 8

def test_user_parentheses_flow():
    expression = "(2+3)*4"
    result = calculate(expression)
    assert result == 20