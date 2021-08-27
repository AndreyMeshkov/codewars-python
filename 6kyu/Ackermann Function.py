# Ackermann Function
#
# https://www.codewars.com/kata/53ad69892a27079b34000bd9
#
# The Ackermann function is a famous function that played a big role in computability theory as the first example of a total computable function that is not primitive recursive.
#
# Since then the function has been a bit simplified but is still of good use. Due to its definition in terms of extremely deep recursion it can be used as a benchmark of a compiler's ability to optimize recursion.
#
# The goal of this kata is to code a function which will be given two inputs, m and n, and will return the Ackermann number A(m,n) defined by:
#
# A(m,n) = n+1                          if m=0
# A(m,n) = A(m-1,1)                     if m>0 , n=0
# A(m,n) = A(m-1,A(m,n-1))              if m,n > 0
# m,n should be non-negative integers, the function should return null (Javascript), None (Python), or nil (Ruby) for other type, non-integer and negative numbers. In C, input is restricted to integer type.

def Ackermann(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return Ackermann((m - 1), Ackermann(m, n - 1))

# Best practice:
#
# from numbers import Number
#
#
# def Ackermann(m, n):
#     if isinstance(n, Number) and isinstance(m, Number):
#         if m >= 0 and n >= 0:
#             return Ackermann_Aux(m, n)
#
#     return None
#
#
# def Ackermann_Aux(m, n):
#     if m == 0:
#         return n + 1
#
#     if m > 0:
#         if n == 0:
#             return Ackermann_Aux(m - 1, 1)
#
#         if n > 0:
#             return Ackermann_Aux(m - 1, Ackermann_Aux(m, n - 1))

# Clever solution:
#
# def Ackermann(m,n):
#     if m:
#         if n:
#             return Ackermann(m - 1, Ackermann(m, n - 1))
#         return Ackermann(m - 1, 1)
#     return n+1