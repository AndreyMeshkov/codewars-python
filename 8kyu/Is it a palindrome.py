# Is it a palindrome?
#
# https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
#
# Write a function that checks if a given string (case insensitive) is a palindrome.

def is_palindrome(s):
    return s.lower() == s.lower()[::-1]

# Best practice and clever solution:
#
# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]
