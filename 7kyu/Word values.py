# Word values
#
# https://www.codewars.com/kata/598d91785d4ce3ec4f000018
#
# Given a string "abc" and assuming that each letter in the string has a value equal to its position in the alphabet, our string will have a value of 1 + 2 + 3 = 6. This means that: a = 1, b = 2, c = 3 ....z = 26.
#
# You will be given a list of strings and your task will be to return the values of the strings as explained above multiplied by the position of that string in the list. For our purpose, position begins with 1.
#
# nameValue ["abc","abc abc"] should return [6,24] because of [ 6 * 1, 12 * 2 ]. Note how spaces are ignored.
#
# "abc" has a value of 6, while "abc abc" has a value of 12. Now, the value at position 1 is multiplied by 1 while the value at position 2 is multiplied by 2.
#
# Input will only contain lowercase characters and spaces.
#
# Good luck!
#
# If you like this Kata, please try:
#
# String matchup
#
# Consonant value

def name_value(my_list):
    for i in range(len(my_list)):
        sum_chars = 0
        for j in my_list[i]:
            if j.isalpha():
                sum_chars += ord(j) - 96
        my_list[i] = sum_chars * (i + 1)
    return my_list

# Best practice and clever solution:
#
# def nameValue(myList):
#     return [ i*sum(map(lambda c: [0, ord(c)-96][c.isalpha()], w.lower())) for i,w in enumerate(myList,1)]
