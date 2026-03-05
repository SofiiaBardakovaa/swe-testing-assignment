def calculate(expression):
    try:
        return eval(expression)
    except ZeroDivisionError:
        return "Error"