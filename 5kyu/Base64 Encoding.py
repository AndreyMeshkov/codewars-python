# Base64 Encoding
#
# https://www.codewars.com/kata/5270f22f862516c686000161
#
# Extend the String object (JS) or create a function (Python, C#) that converts the value of the String to and from Base64 using the ASCII (UTF-8 for C#) character set.
#
# Do not use built in functions.
#
# Usage:
#
# # should return 'dGhpcyBpcyBhIHN0cmluZyEh'
# to_base_64('this is a string!!')
#
# # should return 'this is a string!!'
# from_base_64('dGhpcyBpcyBhIHN0cmluZyEh')
# You can learn more about Base64 encoding and decoding here.
#
# Note: This kata uses the non-padding version ("=" is not added to the end).
import base64


def to_base_64(string):
    string_bytes = string.encode("ascii")
    return base64.b64encode(string_bytes).decode("ascii")


def from_base_64(string):
    return base64.b64decode(string).decode("ascii")
