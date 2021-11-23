# Factorial decomposition
#
# https://www.codewars.com/kata/5a045fee46d843effa000070
#
# The aim of the kata is to decompose n! (factorial n) into its prime factors.
#
# Examples:
#
# n = 12; decomp(12) -> "2^10 * 3^5 * 5^2 * 7 * 11"
# since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
#
# n = 22; decomp(22) -> "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19"
#
# n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23
# Prime numbers should be in increasing order. When the exponent of a prime is 1 don't put the exponent.
#
# Notes
#
# the function is decomp(n) and should return the decomposition of n! into its prime factors in increasing order of the primes, as a string.
# factorial can be a very big number (4000! has 12674 digits, n can go from 300 to 4000).
# In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.

def decomp(n):
    obj = {}
    for i in range(2, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            while i % j == 0:
                i = i // j
                if j in obj:
                    obj[j] += 1
                else:
                    obj[j] = 1
        if i in obj:
            obj[i] += 1
        else:
            obj[i] = 1
    del obj[1]
    return ' * '.join(
        ["{}^{}".format(i, obj[i]) if obj[i] > 1 else str(i) for i in
         sorted(obj)])

# Best practice:
#
# from collections import defaultdict
#
#
# def dec(n):
#     decomp = defaultdict(lambda: 0)
#     i = 2
#     while n > 1:
#         while n % i == 0:
#             n /= i
#             decomp[i] += 1
#         i += 1
#     return decomp
#
#
# def decomp(n):
#     ans = defaultdict(lambda: 0)
#     for i in range(2, n + 1):
#         for key, value in dec(i).items():
#             ans[key] += value
#     return ' * '.join('{}^{}'.format(x, y) if y > 1 else str(x) for x, y in
#                       sorted(ans.items()))

# Clever solution:
#
# is_prime = lambda n: n == 2 or n % 2 and all(n % d for d in range(3, int(n ** .5) + 1, 2))
# order = lambda n, k: n and n // k + order(n // k, k)
# decomp = lambda n: ' * '.join(str(p) if n < 2 * p else '%d^%d' % (p, order(n, p)) for p in range(2, n+1) if is_prime(p))