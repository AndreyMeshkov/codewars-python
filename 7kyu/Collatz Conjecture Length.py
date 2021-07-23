# Collatz Conjecture Length
#
# https://www.codewars.com/kata/54fb963d3fe32351f2000102
#
# The Collatz Conjecture states that for any natural number n, if n is even, divide it by 2. If n is odd, multiply it by 3 and add 1. If you repeat the process continuously for n, n will eventually reach 1.
#
# For example, if n = 20, the resulting sequence will be:
#
# [20, 10, 5, 16, 8, 4, 2, 1]
#
# Write a program that will output the length of the Collatz Conjecture for any given n. In the example above, the output would be 8.
#
# For more reading see: http://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(n):
    result = 1
    while n != 1:
        result += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    return result

# Best practice:
#
# def collatz(n):
#   l = 1
#   while n > 1:
#     l += 1
#     if n % 2 == 0: n /= 2
#     else: n = n * 3 + 1
#   return l
#
# Clever solution:
#
# def collatz(n,c=1):
#     return collatz(n/2,c+1) if n%2==0 else (collatz(n*3+1,c+1) if n!= 1 else c)
