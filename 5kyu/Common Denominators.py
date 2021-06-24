# Common Denominators
#
# https://www.codewars.com/kata/54d7660d2daf68c619000d95
#
# Common denominators
#
# You will have a list of rationals in the form
#
# { {numer_1, denom_1} , ... {numer_n, denom_n} }
# or
# [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
# or
# [ (numer_1, denom_1) , ... (numer_n, denom_n) ]
# where all numbers are positive ints. You have to produce a result in the form:
#
# (N_1, D) ... (N_n, D)
# or
# [ [N_1, D] ... [N_n, D] ]
# or
# [ (N_1', D) , ... (N_n, D) ]
# or
# {{N_1, D} ... {N_n, D}}
# or
# "(N_1, D) ... (N_n, D)"
# depending on the language (See Example tests) in which D is as small as possible and
#
# N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
# Example:
# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12), (3, 12)]
# Note:
# Due to the fact that the first translations were written long ago - more than 6 years - these first translations have only irreducible fractions.
#
# Newer translations have some reducible fractions. To be on the safe side it is better to do a bit more work by simplifying fractions even if they don't have to be.
#
# Note for Bash:
# input is a string, e.g "2,4,2,6,2,8" output is then "6 12 4 12 3 12"

from fractions import gcd
from functools import reduce


def convert_fracts(lst):
    if len(lst) == 0:
        return []
    denums = tuple(i[1] for i in lst)
    lc = lcmm(*denums)
    return [[i[0] * (lc // i[1]), lc] for i in lst]


def lcmm(*numbers):
    def lcm(a, b):
        return (a * b) // gcd(a, b)

    return reduce(lcm, numbers)

# Best practice and clever solution:
#
# import math
# import functools
#
# def convertFracts(lst):
#     lcm = lambda a, b : abs(a*b) // math.gcd(a, b)
#     tmp_list = list(map(lambda x : x[1] ,list(lst)))
#     lcm_num = functools.reduce(lcm,tmp_list)
#     return list(map(lambda x : [x[0] * lcm_num // x[1], lcm_num] , list(lst)))
