def add(num3, num2):
    """Returns the sum of two numbers."""
    return num3 + num2

def subtract(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def multiply(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def rem(num1, num2):
    """Returns the remainder of two numbers."""
    return num1 % num2

def divide(num1, num2):
    """Returns the quotient of two numbers."""
    if num2 == 0:
        raise ValueError("Cannot divide by zero.")
    return num1 / num2
