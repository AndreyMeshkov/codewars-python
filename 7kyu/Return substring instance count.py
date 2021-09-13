# Return substring instance count
#
# https://www.codewars.com/kata/5168b125faced29f66000005
#
# Complete the solution so that it returns the number of times the search_text is found within the full_text.
#
# Usage example:
#
# solution('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up twice
# solution('aaabbbcccc', 'bbb') # should return 1

def solution(full_text, search_text):
    return full_text.count(search_text)

# Best practice:
#
# def solution(full_text, search_text):
#     return full_text.count(search_text)

# Clever solution:
#
# solution = str.count
