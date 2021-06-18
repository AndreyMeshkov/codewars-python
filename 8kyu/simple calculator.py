# simple calculator
#
# https://www.codewars.com/kata/5810085c533d69f4980001cf
#
# You are required to create a simple calculator that returns the result of addition, subtraction, multiplication or division of two numbers.
#
# Your function will accept three arguments:
# The first and second argument should be numbers.
# The third argument should represent a sign indicating the operation to perform on these two numbers.
#
# if the variables are not numbers or the sign does not belong to the list above a message "unknown value" must be returned.
#
# Example:
# calculator(1, 2, '+') => 3
# calculator(1, 2, '$') # result will be "unknown value"

def calculator(x, y, op):
    if (type(x) == int or type(x) == float) and (
            type(y) == int or type(y) == float):
        if op == "+":
            return x + y
        elif op == '-':
            return x - y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
    return "unknown value"

# Best practice and clever solution:
#
# def calculator(x, y, op):
#   return eval(f'{x}{op}{y}') if type(x) == type(y) == int and str(op) in '+-*/' else 'unknown value'
