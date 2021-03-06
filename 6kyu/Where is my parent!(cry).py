# Where is my parent!?(cry)
#
# https://www.codewars.com/kata/58539230879867a8cd00011c
#
# Mothers arranged a dance party for the children in school. At that party, there are only mothers and their children. All are having great fun on the dance floor when suddenly all the lights went out. It's a dark night and no one can see each other. But you were flying nearby and you can see in the dark and have ability to teleport people anywhere you want.
#
# Legend:
# -Uppercase letters stands for mothers, lowercase stand for their children, i.e. "A" mother's children are "aaaa".
# -Function input: String contains only letters, uppercase letters are unique.
# Task:
# Place all people in alphabetical order where Mothers are followed by their children, i.e. "aAbaBb" => "AaaBbb".

def find_children(dancing_brigade):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        if (
                letter in dancing_brigade or letter.upper() in dancing_brigade) and (
                result.find(letter) == -1 and result.find(
            letter.upper()) == -1):
            result += dancing_brigade.count(letter.upper()) * letter.upper()
            result += dancing_brigade.count(letter) * letter
    return result

# Best practice:
#
# def find_children(dancing_brigade):
#     return ''.join(sorted(dancing_brigade,key=lambda c:(c.upper(),c.islower())))


# Clever solution:
#
# def find_children(s):
#     return ''.join( sorted(sorted(s), key=str.lower) )