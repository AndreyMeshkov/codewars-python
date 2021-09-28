# Remove the parentheses
#
# https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8
#
# Remove the parentheses
# In this kata you are given a string for example:
#
# "example(unwanted thing)example"
# Your task is to remove everything inside the parentheses as well as the parentheses themselves.
#
# The example above would return:
#
# "exampleexample"
# Notes
# Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
# There can be multiple parentheses.
# The parentheses can be nested.

def remove_parentheses(s):
    parentheses_count = 0
    output = ""
    for i in s:
        if i == "(":
            parentheses_count += 1
        elif i == ")":
            parentheses_count -= 1
        else:
            if parentheses_count == 0:
                output += i
    return output

# Best practice and clever solution:
#
# def remove_parentheses(s):
#     lvl,out = 0,[]
#     for c in s:
#         lvl += c=='('
#         if not lvl: out.append(c)
#         lvl -= c==')'
#     return ''.join(out)