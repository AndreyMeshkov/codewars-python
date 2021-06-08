# Name Shuffler
#
# https://www.codewars.com/kata/559ac78160f0be07c200005a
#
# Write a function that returns a string in which firstname is swapped with last name.
#
# name_shuffler('john McClane'); => "McClane john"

def name_shuffler(str_):
    list_ = str_.split(' ')
    list_.reverse()
    return ' '.join(list_)

# Best practice and clever solution:
#
# def name_shuffler(str_):
#     return ' '.join(str_.split(' ')[::-1])
