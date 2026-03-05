from calculator_logic import calculate

# addition
def test_addition():
    assert calculate("2+3") == 5

# subtraction
def test_subtraction():
    assert calculate("5-2") == 3

# multiplication
def test_multiplication():
    assert calculate("4*3") == 12

# division
def test_division():
    assert calculate("10/2") == 5

# parentheses
def test_parentheses():
    assert calculate("(2+3)*4") == 20

# edge case: division by zero
def test_division_by_zero():
    assert calculate("5/0") == "Error"

# edge case: negative numbers
def test_negative_numbers():
    assert calculate("-5+2") == -3

# edge case: decimal numbers
def test_decimal_numbers():
    assert calculate("5.5+2.5") == 8.0