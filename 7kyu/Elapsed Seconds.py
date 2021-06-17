# Elapsed Seconds
#
# https://www.codewars.com/kata/517b25a48557c200b800000c
#
# Complete the function so that it returns the number of seconds that have elapsed between the start and end times given.
#
# Tips:
# The start/end times are given as Date (JS/CoffeeScript), DateTime (C#), Time (Nim), datetime(Python) and Time (Ruby) instances.
# The start time will always be before the end time.

def elapsed_seconds(start, end):
    from time import mktime

    return mktime(end.timetuple()) - mktime(start.timetuple())

# Best practice:
#
# def elapsed_seconds(start, end):
#     return (end - start).total_seconds()
#
# Clever solution:
#
# def elapsed_seconds(start, end):
#     return (end-start).seconds
