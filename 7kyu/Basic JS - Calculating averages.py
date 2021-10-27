# Basic JS - Calculating averages
#
# https://www.codewars.com/kata/529f32794a6db5d32a00071f
#
# Let's build a calculator that can calculate the average for an arbitrary number of arguments.
#
# The test expects you to provide a Calculator object with an average method:
#
# Calculator.average()
# The test also expects that when you pass no arguments, it returns 0. The arguments are expected to be integers.
#
# It expects Calculator.average(3,4,5) to return 4.

class Calculator:
    @staticmethod
    def average(*args):
        return sum(args) / len(args) if args else 0

# Best practice:
#
# class Calculator:
#     @staticmethod
#     def average(*_a):
#         return sum( _a ) / len( _a ) if len( _a ) >  0 else 0
#
# Clever solution:
#
# from statistics import mean
#
#
# class Calculator:
#     @staticmethod
#     def average(*args):
#         return len(args) and mean(args)
