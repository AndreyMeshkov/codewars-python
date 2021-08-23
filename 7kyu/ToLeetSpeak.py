# ToLeetSpeak
#
# https://www.codewars.com/kata/57c1ab3949324c321600013f
#
# Your task is to write a function toLeetSpeak that converts a regular english sentence to Leetspeak.
#
# More about LeetSpeak You can read at wiki -> https://en.wikipedia.org/wiki/Leet
#
# Consider only uppercase letters (no lowercase letters, no numbers) and spaces.
#
# For example:
#
# toLeetSpeak("LEET") returns "1337"
# In this kata we use a simple LeetSpeak dialect. Use this alphabet:

obj = {
    "A": '@',
    "B": '8',
    "C": '(',
    "D": 'D',
    "E": '3',
    "F": 'F',
    "G": '6',
    "H": '#',
    "I": '!',
    "J": 'J',
    "K": 'K',
    "L": '1',
    "M": 'M',
    "N": 'N',
    "O": '0',
    "P": 'P',
    "Q": 'Q',
    "R": 'R',
    "S": '$',
    "T": '7',
    "U": 'U',
    "V": 'V',
    "W": 'W',
    "X": 'X',
    "Y": 'Y',
    "Z": '2'
}


def to_leet_speak(str):
    result = ""
    for i in str:
        if i in obj:
            result += obj[i]
        else:
            result += i
    return result

# Best practice and clever solution:
#
# def to_leet_speak(str):
#     return str.translate(str.maketrans("ABCEGHILOSTZ", "@8(36#!10$72"))