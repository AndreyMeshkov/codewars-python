# Last digit of a large number
#
# https://www.codewars.com/kata/5511b2f550906349a70004e1
import math


def last_digit(n1, n2):
    str_n1 = str(n1)
    str_n2 = str(n2)
    len_n1 = len(str_n1)
    len_n2 = len(str_n2)
    if (len_n2 == 1 and str_n2 == '0'):
        return 1
    if (len_n1 == 1 and str_n1 == '0'):
        return 0
    if ((Modulo(4, str_n2) == 0)):
        exp = 4
    else:
        exp = Modulo(4, str_n2)
    res = math.pow(int(str_n1[len_n1 - 1]), exp)
    return res % 10


def Modulo(a, b):
    mod = 0
    for i in range(0, len(b)):
        mod = (mod * 10 + int(b[i])) % a
    return mod

# Best practice and clever solution:
#
# def last_digit(n1, n2):
#     return pow( n1, n2, 10 )
