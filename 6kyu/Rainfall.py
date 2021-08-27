# Rainfall
#
# https://www.codewars.com/kata/56a32dd6e4f4748cc3000006
#
# dataand data1 are two strings with rainfall records of a few cities for months from January to December. The records of towns are separated by \n. The name of each town is followed by :.
#
# data and towns can be seen in "Your Test Cases:".
#
# Task:
# function: mean(town, strng) should return the average of rainfall for the city town and the strng data or data1 (In R and Julia this function is called avg).
# function: variance(town, strng) should return the variance of rainfall for the city town and the strng data or data1.
# Examples:
# mean("London", data), 51.19(9999999999996)
# variance("London", data), 57.42(833333333374)
# Notes:
# if functions mean or variance have as parameter town a city which has no records return -1 or -1.0 (depending on the language)
# Don't truncate or round: the tests will pass if abs(your_result - test_result) <= 1e-2 or abs((your_result - test_result) / test_result) <= 1e-6 depending on the language.
# Shell tests only variance
# A ref: http://www.mathsisfun.com/data/standard-deviation.html
# data and data1 (can be named d0 and d1 depending on the language; see "Sample Tests:") are adapted from: http://www.worldclimate.com

import numpy as np


def mean(town, strng):
    dct = create_dict(strng)
    if town in dct:
        return sum(dct[town]) / len(dct[town])
    else:
        return -1


def variance(town, strng):
    dct = create_dict(strng)
    if town in dct:
        return np.var(dct[town])
    else:
        return -1


def create_dict(strng):
    obj = {}
    data = strng.split("\n")
    for i in data:
        lst = i.split(":")
        obj[lst[0]] = lst[1].split(",")
        for j in range(len(obj[lst[0]])):
            obj[lst[0]][j] = float(obj[lst[0]][j].split(" ")[1])
    return obj

# Best practice:
#
#
# def get_towndata(town, strng):
#     for line in strng.split('\n'):
#         s_town, s_data = line.split(':')
#         if s_town == town:
#             return [s.split(' ') for s in s_data.split(',')]
#     return None
#
#
# def mean(town, strng):
#     data = get_towndata(town, strng)
#     if data is not None:
#         return sum([float(x) for m, x in data]) / len(data)
#     else:
#         return -1.
#
#
# def variance(town, strng):
#     data = get_towndata(town, strng)
#     if data is not None:
#         mean = sum([float(x) for m, x in data]) / len(data)
#         return sum([(float(x) - mean) ** 2 for m, x in data]) / len(data)
#     else:
#         return -1.

# Clever solution:
#
# import statistics, re
#
# rain = lambda town, strng: map(float, re.findall("\d+(?:\.\d+)?", "".join(re.findall(town+":(.+)\n", strng))))
#
# def mean(town, strng):
#     return statistics.mean(rain(town, strng))
# def variance(town, strng):
#     return statistics.pvariance(rain(town, strng))