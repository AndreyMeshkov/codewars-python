# Primorial Of a Number
#
# https://www.codewars.com/kata/5a99a03e4a6b34bb3c000124
#
# Definition (Primorial Of a Number)
# Is similar to factorial of a number, In primorial, not all the natural numbers get multiplied, only prime numbers are multiplied to calculate the primorial of a number. It's denoted with P# and it is the product of the first n prime numbers.
#
# Task
# Given a number N , calculate its primorial.!alt!alt
# Notes
# Only positive numbers will be passed (N > 0) .
# Input >> Output Examples:
# 1- numPrimorial (3) ==> return (30)
# Explanation:
# Since the passed number is (3) ,Then the primorial should obtained by multiplying 2 * 3 * 5 = 30 .
#
# Mathematically written as , P3# = 30 .
# 2- numPrimorial (5) ==> return (2310)
# Explanation:
# Since the passed number is (5) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 = 2310 .
#
# Mathematically written as , P5# = 2310 .
# 3- numPrimorial (6) ==> return (30030)
# Explanation:
# Since the passed number is (6) ,Then the primorial should obtained by multiplying 2 * 3 * 5 * 7 * 11 * 13 = 30030 .
#
# Mathematically written as , P6# = 30030 .

def num_primorial(n):
    if n == 1:
        return 2
    i = 3
    count = 1
    result = 2
    while (count < n):
        if isprime(i):
            count += 1
            result *= i
        i += 2
    return result


def isprime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    else:
        return True

# Best practice and clever solution:
#
# def num_primorial(n):
#     primorial, x, n = 2, 3, n-1
#     while n:
#         if all(x % d for d in range(3, int(x ** .5) + 1, 2)):
#             primorial *= x
#             n -= 1
#         x += 2
#     return primorial
