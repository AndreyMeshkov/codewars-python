# Clocky Mc Clock-Face
#
# https://www.codewars.com/kata/59752e1f064d1261cb0000ec
#
# Story
# Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.
#
# And because the local council has lost most of our tax money to a Nigerian email scam there are no funds to fix the clock properly.
#
# Instead, they are asking for volunteer programmers to write some code that tell the time by only looking at the remaining hour-hand!
#
# What a bunch of cheapskates!
#
# Can you do it?
#
# Kata
# Given the angle (in degrees) of the hour-hand, return the time in HH:MM format. Round down to the nearest minute.
#
# Examples
# 12:00 = 0 degrees
# 03:00 = 90 degrees
# 06:00 = 180 degrees
# 09:00 = 270 degrees
# 12:00 = 360 degrees
# Notes
# 0 <= angle <= 360

def what_time_is_it(angle):
    minutes = angle * 2
    h = str(int(minutes / 60))
    m = str(int(minutes % 60))
    if h == "0":
        h = "12"
    return h.zfill(2) + ":" + m.zfill(2)

# Best practice:
#
# def what_time_is_it(angle):
#     hr = int(angle // 30)
#     mn = int((angle % 30) * 2)
#     if hr == 0:
#         hr = 12
#     return '{:02d}:{:02d}'.format(hr, mn)

# Clever solution:
#
# def what_time_is_it(angle):
#     angle %= 360
#     h, m = divmod(angle, 30)
#     return '{:02}:{:02}'.format(int(h or 12), int(m * 2))