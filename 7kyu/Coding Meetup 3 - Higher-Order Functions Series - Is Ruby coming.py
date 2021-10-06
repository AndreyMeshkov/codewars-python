# Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?
#
# https://www.codewars.com/kata/5827acd5f524dd029d0005a4
#
# You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if at least one Ruby developer has signed up; or
# false if there will be no Ruby developers.
# For example, given the following input array:
#
# list1 = [
#     { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35, 'language': 'Java' },
#     { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language': 'Python' },
#     { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, 'language': 'Ruby' }
#     ]
# your function should return true.
#
# Notes:
#
# The input array will always be valid and formatted as in the example above.
#
# This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible.

def is_ruby_coming(lst):
    for person in lst:
        if person["language"] == "Ruby":
            return True
    return False

# Best practice and clever solution:
#
# def is_ruby_coming(lst):
#     return any(x["language"] == "Ruby" for x in lst)

