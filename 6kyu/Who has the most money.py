# Who has the most money?
#
# https://www.codewars.com/kata/528d36d7cc451cd7e4000339
#
# You're going on a trip with some students and it's up to you to keep track of how much money each Student has. A student is defined like this:
#
# class Student:
#     def __init__(self, name, fives, tens, twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
# As you can tell, each Student has some fives, tens, and twenties. Your job is to return the name of the student with the most money. If every student has the same amount, then return "all".
#
# Notes:
#
# Each student will have a unique name
# There will always be a clear winner: either one person has the most, or everyone has the same amount
# If there is only one student, then that student has the most money
#
class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties


def most_money(students):
    money = []
    for student in students:
        money.append(
            student.fives * 5 + student.tens * 10 + student.twenties * 20)
    num = max(money)
    ind = money.index(num)
    count = money.count(num)
    if count == len(money) and len(money) > 1:
        return "all"
    else:
        return students[ind].name

# Best practice and clever solution:
#
# def most_money(students):
#     total = []
#     for student in students:
#         total.append(
#             (student.fives * 5) + (student.tens * 10) + (student.twenties * 20))
#
#     if min(total) == max(total) and len(students) > 1:
#         return "all"
#     else:
#         return students[total.index(max(total))].name
