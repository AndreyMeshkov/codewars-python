# Get number from string
#
# https://www.codewars.com/kata/57a37f3cbb99449513000cd8
#
# Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56
#
# Function: ####javascript
#
# getNumberFromString(s)
# ####ruby
#
# get_number_from_string(s)
# ####CSharp
#
# GetNumberFromString(string s)

def get_number_from_string(string):
    result = ''
    for ch in string:
        if ch.isdigit():
            result += ch
    return int(result)

# Best practice:
#
# def get_number_from_string(string):
#     return int(''.join(x for x in string if x.isdigit()))
#
# Clever solution:
#
# import re
#
# def get_number_from_string(s):
#     return int(re.sub(r'\D', '', s))
