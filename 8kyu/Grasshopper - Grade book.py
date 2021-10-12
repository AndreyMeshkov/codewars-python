# Grasshopper - Grade book
#
# https://www.codewars.com/kata/55cbd4ba903825f7970000f5
#
# Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
#
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    avg = (s1 + s2 + s3) / 3
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

# Best practice:
#
# def get_grade(s1, s2, s3):
#     m = (s1 + s2 + s3) / 3.0
#     if 90 <= m <= 100:
#         return 'A'
#     elif 80 <= m < 90:
#         return 'B'
#     elif 70 <= m < 80:
#         return 'C'
#     elif 60 <= m < 70:
#         return 'D'
#     return "F"

# Clever solution:
#
# def get_grade(s1, s2, s3):
#     return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
