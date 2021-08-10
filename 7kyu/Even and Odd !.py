# Even and Odd !
#
# https://www.codewars.com/kata/594adadee075005308000122
#
# Given a number N, can you fabricate two numbers NE and NO such as NE is formed by even digits of N and NO is formed by odd digits of N? Examples:
#
# 126453 -> NE = 264, NO = 153
# 3012 -> NE = 2, NO = 31
# 4628 -> NE = 4628, NO = 0 0 is considered as an even number.
# In C you should return an array of two elements such as the first is NE and the second is NO.

def even_and_odd(n):
    n_even = "0"
    n_odd = "0"
    for i in str(n):
        if int(i) % 2 == 0:
            n_odd += i
        else:
            n_even += i
    return (int(n_odd), int(n_even))

# Best practice and clever solution:
#
# def even_and_odd(n):
#     ne = "".join(x for x in str(n) if x in "02468")
#     no = "".join(y for y in str(n) if int(y) % 2)
#     return tuple(0 if not a else int(a) for a in (ne, no))