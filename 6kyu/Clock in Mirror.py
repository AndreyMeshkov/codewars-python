# Clock in Mirror
#
# https://www.codewars.com/kata/56548dad6dae7b8756000037
#
# Peter can see a clock in the mirror from the place he sits in the office. When he saw the clock shows 12:22
#
# He knows that the time is 11:38
#
# in the same manner:
#
# 05:25 --> 06:35
#
# 01:50 --> 10:10
#
# 11:58 --> 12:02
#
# 12:01 --> 11:59
#
# Please complete the function WhatIsTheTime(timeInMirror), where timeInMirror is the mirrored time (what Peter sees) as string.
#
# Return the real time as a string.
#
# Consider hours to be between 1 <= hour < 13.
#
# So there is no 00:20, instead it is 12:20.
#
# There is no 13:20, instead it is 01:20.

def what_is_the_time(time_in_mirror):
    hour = int(time_in_mirror[0:2])
    minute = int(time_in_mirror[3:5])

    if hour < 11:
        hour1 = 11 - hour
    else:
        hour1 = 23 - hour

    minute1 = 60 - minute
    if minute1 == 60:
        minute1 -= 60
        hour1 += 1
    if hour1 > 12:
        hour1 -= 12

    if hour1 > 9:
        result = str(hour1) + ':'
    else:
        result = '0' + str(hour1) + ':'

    if minute1 > 9:
        result += str(minute1)
    else:
        result += '0' + str(minute1)
    return result

# Best practice and clever solution:
#
# def what_is_the_time(time_in_mirror):
#     h, m = map(int, time_in_mirror.split(':'))
#     return '{:02}:{:02}'.format(-(h + (m != 0)) % 12 or 12, -m % 60)
