# Complete Fibonacci Series
#
# https://www.codewars.com/kata/5239f06d20eeab9deb00049b
#
# The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number as an argument to decide how many no. of elements to produce. If the argument is less than or equal to 0 then return empty array
#
# Example:
#
# fibonacci(4) # should return  [0,1,1,2]
# fibonacci(-1) # should return []
from urllib3.connectionpool import xrange


def fibonacci(n):
    fib = [0, 1]
    for i in xrange(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[0: n] if n >= 0 else []

# Best practie:
#
# def fibonacci(n):
#     if n<=0:
#       return []
#     a = 0
#     b = 1
#     l = [0]
#     for i in range(n):
#         a,b = b, a+b
#         l.append(a)
#     return l[0:n]

# Clever solution:
#
# def fibonacci(n):
#     if n <= 0: return []
#     res = []
#     i, j = 0, 1
#     while n:
#         res.append(i)
#         i, j = j, i+j
#         n -= 1
#     return res