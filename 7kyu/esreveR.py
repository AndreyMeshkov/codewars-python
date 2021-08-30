# esreveR
#
# https://www.codewars.com/kata/5413759479ba273f8100003d
#
# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)
#
# (the dedicated builtin(s) functionalities are deactivated)

def reverse(lst):
    empty_list = list()
    while len(lst) > 0:
        empty_list.append(lst.pop())
    return empty_list

# Best practice:
#
# def reverse(lst):
#     out = list()
#     for i in range(len(lst)-1,-1,-1):
#         out.append(lst[i])
#     return out
#
# Clever solution:
#
# def reverse(lst):
#     empty_list = list()
#     for i in range(len(lst)):
#         empty_list.append(lst.pop())
#     return empty_list