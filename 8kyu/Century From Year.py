# Century From Year
#
# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
#
# Introduction
# The first century spans from the year 1 up to and including the year 100, The second - from the year 101 up to and including the year 200, etc.
#
# Task :
# Given a year, return the century it is in.
#
# Input , Output Examples :
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# Hope you enjoy it .. Awaiting for Best Practice Codes
#
# Enjoy Learning !!!
import math


def century(year):
    return math.ceil(year / 100)

# Best practice and clever solution:
#
# def century(year):
#     return (year + 99) // 100
