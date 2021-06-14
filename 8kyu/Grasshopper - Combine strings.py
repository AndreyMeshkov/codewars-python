# Grasshopper - Combine strings
#
# https://www.codewars.com/kata/55f73f66d160f1f1db000059
#
# Combine strings function
# Create a function named (combine_names) that accepts two parameters (first and last name). The function should return the full name.
#
# Example:
#
# combine_names('James', 'Stevens')
# returns:
#
# 'James Stevens'

def combine_names(name, last_name):
    return f'{name} {last_name}'

# Best practice:
#
# def combine_names(first, last):
#     return first + " " + last
#
# Clever solution:
#
# def combine_names(*args):
#     return ' '.join(args)
