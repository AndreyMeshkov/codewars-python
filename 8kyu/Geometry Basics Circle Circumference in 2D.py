# Geometry Basics: Circle Circumference in 2D
#
# https://www.codewars.com/kata/58e43389acfd3e81d5000a88
#
# This series of katas will introduce you to basics of doing geometry with computers.
#
# Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.
#
# Write a function calculating circumference of a Circle.
#
# Tests round answers to 6 decimal places.
import math


def circle_circumference(circle):
    return circle.radius * 2 * math.pi

# Best practice:
#
# from math import pi
#
# def circle_circumference(circle):
#     return round(2 * circle.radius * pi, 6)
#
# Clever solution:
#
# circle_circumference = lambda c: 2*c.radius*3.14159265359
