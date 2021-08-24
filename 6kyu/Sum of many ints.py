# Sum of many ints
#
# https://www.codewars.com/kata/54c2fc0552791928c9000517
#
# Write this function
#
#
# for i from 1 to n, do i % m and return the sum
#
# f(n=10, m=5) // returns 20 (1+2+3+4+0 + 1+2+3+4+0)
# You'll need to get a little clever with performance, since n can be a very large number

def f(n, m):
    return (n // m) * m * (m - 1) / 2 + (n % m) * (n % m + 1) / 2

# Best practice and clever solution:
#
# def f(n, m):
#     re, c = divmod(n,m)
#     return m*(m-1)/2*re + (c+1)*c/2
