# Christmas tree
#
# https://www.codewars.com/kata/52755006cc238fcae70000ed
#
# Create a function that returns a christmas tree of the correct height.
#
# For example:
#
# hieght = 5 should return:
#
#     *
#    ***
#   *****
#  *******
# *********
# Height passed is always an integer between 0 and 100.
#
# Use \n for newlines between each line.
#
# Pad with spaces so each line is the same length. The last line having only stars, no spaces.

def christmas_tree(height):
    length = height * 2 - 1
    string = ""
    count = 1
    while count <= height:
        if count > 1:
            string += '\n'
        string += f"{' ' * int((length - (count * 2 - 1)) / 2)}{'*' * (count * 2 - 1)}{' ' * int((length - (count * 2 - 1)) / 2)}"
        count += 1
    return string

# Best practice and clever solution:
#
# def christmas_tree(height: int) -> str:
#     return '\n'.join(('*' * i).center(2 * height - 1) for i in range(1, height * 2, 2))
