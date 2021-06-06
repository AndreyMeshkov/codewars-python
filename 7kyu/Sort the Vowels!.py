# Sort the Vowels!
#
# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a
#
# Sort the Vowels!
# In this kata, we want to sort the vowels in a special format.
#
# Task
# Write a function which takes a input string s and return a string in the following way:
# C | R |
# | O
# n |
# D | d |
# "Codewars" = > | E
# "Rnd Te5T" = > |
# W | T |
# | A | e
# R | 5 |
# S | T |
# Notes:
#
# List all the Vowels on the right side of |
# List every character except Vowels on the left side of |
# Case doesn't matter
# Each line is seperated with \n
# Invalid input ( undefined / null / integer ) should return an empty string

def sort_vowels(s):
    if type(s) != str:
        return ''
    vowels = 'aoeiuAOEIU'
    result = ''
    for ch in s:
        if vowels.find(ch) == -1:
            result += f'{ch}|\n'
        else:
            result += f'|{ch}\n'
    return result[:-1]

# Best practice and clever solution:
#
# def sort_vowels(s):
#     return "" if not isinstance(s, str) else "\n".join("|" + x if x in "aeiouAEIOU" else x + "|" for x in s)
