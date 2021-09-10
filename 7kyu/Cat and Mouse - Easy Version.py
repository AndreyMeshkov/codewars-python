# Cat and Mouse - Easy Version
#
# https://www.codewars.com/kata/57ee24e17b45eff6d6000164
#
# You will be given a string (x) featuring a cat 'C' and a mouse 'm'. The rest of the string will be made up of '.'.
#
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump over three characters. So:
#
# C.....m returns 'Escaped!' <-- more than three characters between
#
# C...m returns 'Caught!' <-- as there are three characters between the two, the cat can jump.

def cat_mouse(x):
    return "Caught!" if len(x) < 6 else "Escaped!"

# Best practice:
#
# def cat_mouse(x):
#     return 'Escaped!' if x.count('.') > 3 else 'Caught!'

# Clever solution:
#
# def cat_mouse(x):
#     if len(x) > 5:
#         return "Escaped!"
#     else:
#         return "Caught!"
