# Total amount of points
#
# https://www.codewars.com/kata/5bb904724c47249b10000131
#
# Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.
#
# For example: ["3:1", "2:2", "0:1", ...]
#
# Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:
#
# if x>y - 3 points
# if x<y - 0 point
# if x=y - 1 point
# Notes:
#
# there are 10 matches in the championship
# 0 <= x <= 4
# 0 <= y <= 4

def points(games):
    result = 0
    for res in games:
        res_lst = res.split(":")
        if int(res_lst[0]) > int(res_lst[1]):
            result += 3
        elif res_lst[0] == res_lst[1]:
            result += 1
    return result

# Best practice and clever solution:
#
# def points(games):
#     count = 0
#     for score in games:
#         res = score.split(':')
#         if res[0]>res[1]:
#             count += 3
#         elif res[0] == res[1]:
#             count += 1
#     return count
