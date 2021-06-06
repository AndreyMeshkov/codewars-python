# Add Length
#
# https://www.codewars.com/kata/559d2284b5bb6799e9000047
#
# What if we need the length of the words separated by a space to be added at the end of that same word and have it returned as an array?
#
# add_length('apple ban') => ["apple 5", "ban 3"]
# add_length('you will win') => ["you 3", "will 4", "win 3"]
# Your task is to write a function that takes a String and returns an Array/list with the length of each word added to each element .
#
# Note: String will have at least one element; words will always be separated by a space.

def add_length(str_):
    list_word = str_.split(' ')
    result = []
    for word in list_word:
        result.append(f'{word} {len(word)}')
    return result

# Best practice and clever solution:
#
# def add_length(str_):
#     return ["{} {}".format(i, len(i)) for i in str_.split(' ')]
