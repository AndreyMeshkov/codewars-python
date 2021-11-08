# Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?
#
# https://www.codewars.com/kata/58291fea7ff3f640980000f9
#
# You will be given a sequence of objects (associative arrays in PHP) representing data about developers who have signed up to attend the next coding meetup that you are organising.
#
# Your task is to return:
#
# true if all of the following continents / geographic zones will be represented by at least one developer: 'Africa', 'Americas', 'Asia', 'Europe', 'Oceania'.
# false otherwise.
# For example, given the following input array:
#
# list1 =  [
#   { 'firstName': 'Fatima', 'lastName': 'A.', 'country': 'Algeria', 'continent': 'Africa', 'age': 25, 'language': 'JavaScript' },
#   { 'firstName': 'Agustín', 'lastName': 'M.', 'country': 'Chile', 'continent': 'Americas', 'age': 37, 'language': 'C' },
#   { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 39, 'language': 'Ruby' },
#   { 'firstName': 'Laia', 'lastName': 'P.', 'country': 'Andorra', 'continent': 'Europe', 'age': 55, 'language': 'Ruby' },
#   { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 65, 'language': 'PHP' }
#   ]
# your function should return true as there is at least one developer from the required 5 geographic zones.
#
# Notes:
#
# The input array and continent names will always be valid and formatted as in the list above for example 'Africa' will always start with upper-case 'A'.
#
#
#
#
# This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which have been designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: forEach, filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible.
#
# Here is the full list of the katas in the Coding Meetup series:

def all_continents(lst):
    continents = ['Africa', 'Americas', 'Asia', 'Europe', 'Oceania']
    for person in lst:
        if person['continent'] in continents:
            continents.remove(person['continent'])
    return len(continents) == 0

# Best practice and clever solution:
#
# def all_continents(lst):
#     return len(set(x["continent"] for x in lst)) == 5
