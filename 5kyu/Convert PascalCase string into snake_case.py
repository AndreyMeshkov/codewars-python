# Convert PascalCase string into snake_case
#
# https://www.codewars.com/kata/529b418d533b76924600085d
#
# Complete the function/method so that it takes CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If method gets number, it should return string.
#
# Examples:
#
# # returns test_controller
# to_underscore('TestController')
#
# # returns movies_and_books
# to_underscore('MoviesAndBooks')
#
# # returns app7_test
# to_underscore('App7Test')
#
# # returns "1"
# to_underscore(1)

def to_underscore(string):
    if type(string) != str:
        return str(string)
    result = ""
    for letter in string:
        if letter.isalpha() and letter == letter.upper() and string.find(
                letter) != 0:
            result += f"_{letter.lower()}"
        else:
            result += letter.lower()
    return result

# Best practice and clever solution:
#
# import re
#
# def to_underscore(string):
#     return re.sub(r'(.)([A-Z])', r'\1_\2', str(string)).lower()
