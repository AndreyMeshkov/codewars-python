# Correct the mistakes of the character recognition software
#
# https://www.codewars.com/kata/577bd026df78c19bca0002c0
#
# Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.
#
# When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.
#
# Your task is correct the errors in the digitised text. You only have to handle the following mistakes:
#
# S is misinterpreted as 5
# O is misinterpreted as 0
# I is misinterpreted as 1
# The test cases contain numbers only by mistake.

def correct(s):
    return s.replace("5", "S").replace("1", "I").replace("0", "O")

# Best practice and clever solution:
#
# def correct(string):
#     return string.translate(str.maketrans("501", "SOI"))