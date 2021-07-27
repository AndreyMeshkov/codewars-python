# Simple fraction to mixed number converter
#
# https://www.codewars.com/kata/556b85b433fb5e899200003f
#
# Task
# Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:
#
# [sign]a b/c
#
# where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).
#
# If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.
#
# Division by zero should raise an error (preferably, the standard zero division error of your language).
#
# Value ranges
# -10 000 000 < x < 10 000 000
# -10 000 000 < y < 10 000 000
# Examples
# Input: 42/9, expected result: 4 2/3.
# Input: 6/3, expedted result: 2.
# Input: 4/6, expected result: 2/3.
# Input: 0/18891, expected result: 0.
# Input: -10/7, expected result: -1 3/7.
# Inputs 0/0 or 3/0 must raise a zero division error.
# Note
# Make sure not to modify the input of your function in-place, it is a bad practice.

def mixed_fraction(s):
    is_negative = s.count("-") == 1
    numbers = s.split("/")
    num0 = abs(int(numbers[0]))
    num1 = abs(int(numbers[1]))
    if num1 == 0:
        raise
    if num0 == 0:
        return "0"
    integer = str(num0 // num1) + " " if num0 // num1 > 0 else ""
    fraction = ""
    if num0 % num1 > 0:
        gcd_num = gcd(num0 % num1, num1)
        if gcd_num > 1:
            fraction += f"{(num0 % num1) // gcd_num}/{num1 // gcd_num}"
        else:
            fraction += f"{num0 % num1}/{num1}"
    result = f"{integer}{fraction}" if fraction != "" else integer[0:-1]
    return f"-{result}" if is_negative else result


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Best practice and clever solution:
#
# from fractions import Fraction
#
# def mixed_fraction(s):
#     f = Fraction(*map(int, s.split('/')))
#     if f.denominator == 1: return str(f.numerator)
#     n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
#     f = abs(f - n) if n else f - n
#     return "{} {}".format(n, f) if n else str(f)
