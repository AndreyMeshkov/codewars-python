# Remove duplicates from list
#
# https://www.codewars.com/kata/57a5b0dfcf1fa526bb000118
#
# Define a function that removes duplicates from an array of numbers and returns it as a result.
#
# The order of the sequence has to stay the same.

def distinct(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result

# Best practice and clever solution:
#
# def distinct(seq):
#     return sorted(set(seq), key = seq.index)
