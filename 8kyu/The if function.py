# The 'if' function
#
# https://www.codewars.com/kata/54147087d5c2ebe4f1000805
#
# Create a function called _if which takes 3 arguments: a boolean value bool and 2 functions (which do not take any parameters): func1 and func2
#
# When bool is truth-ish, func1 should be called, otherwise call the func2.
#
# Example:
#
# def truthy():
#     print("True")
#
#
# def falsey():
#     print("False")
#
#
# _if(True, truthy, falsey)
# # prints 'True' to the console

def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()

# Best practice:
#
# def _if(bool, func1, func2):
#   func1() if bool else func2()

# Clever solution:
#
# _if = lambda b, t, f: (b and t or f)()
