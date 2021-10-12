# Most Frequent Weekdays
#
# https://www.codewars.com/kata/56eb16655250549e4b0013f4/train/python
#
# What is your favourite day of the week? Check if it's the most frequent day of the week in the year.
#
# You are given a year as integer (e. g. 2001). You should return the most frequent day(s) of the week in that year. The result has to be a list of days sorted by the order of days in week (e. g. ['Monday', 'Tuesday'], ['Saturday', 'Sunday'], ['Monday', 'Sunday']). Week starts with Monday.
#
# Input: Year as an int.
#
# Output: The list of most frequent days sorted by the order of days in week (from Monday to Sunday).
#
# Preconditions:
#
# Week starts on Monday.
# Year is between 1583 and 4000.
# Calendar is Gregorian.
# Example:
#
# most_frequent_days(2427) == ['Friday']
# most_frequent_days(2185) == ['Saturday']
# most_frequent_days(2860) == ['Thursday', 'Friday']

import datetime


def most_frequent_days(year):
    days = []
    first = datetime.date(year, 1, 1)
    end = datetime.date(year, 12, 31)
    if first.weekday() == end.weekday():
        days.append(first.strftime("%A"))
    else:
        if first.weekday() > end.weekday():
            first, end = end, first
        days.append(first.strftime("%A"))
        days.append(end.strftime("%A"))
    return days

# Best practice:
#
# from calendar import weekday
# week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
#
# def most_frequent_days(year):
#     beg = weekday(year, 1, 1)
#     end = weekday(year, 12, 31)
#     if beg == end:
#         return [week[beg]]
#     else:
#         if beg < end:
#             return [week[beg], week[end]]
#         else:
#             return [week[end], week[beg]]

# Clever solution:
#
# from datetime import datetime
# from calendar import day_name
#
#
# def most_frequent_days(year):
#     first = set(range(datetime(year, 1, 1).weekday(), 7))
#     last = set(range(datetime(year, 12, 31).isoweekday()))
#     return [day_name[day] for day in sorted((first & last) or (first | last))]
