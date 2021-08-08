# Convert boolean values to strings 'Yes' or 'No'.
#
# https://www.codewars.com/kata/53369039d7ab3ac506000467
#
# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# Best practice:
#
# def bool_to_word(bool):
#     return "Yes" if bool else "No"
#
# Clever solution:
#
# def bool_to_word(bool):
#     return ['No', 'Yes'][bool]
