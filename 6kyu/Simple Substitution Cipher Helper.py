# Simple Substitution Cipher Helper
#
# https://www.codewars.com/kata/52eb114b2d55f0e69800078d
#
# A
# simple
# substitution
# cipher
# replaces
# one
# character
# from an alphabet
#
# with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.
#
# E.g.
#
# map1 = "abcdefghijklmnopqrstuvwxyz";
# map2 = "etaoinshrdlucmfwypvbgkjqxz";
#
# cipher = Cipher(map1, map2);
# cipher.encode("abc")  # => "eta"
# cipher.encode("xyz")  # => "qxz"
# cipher.encode("aeiou")  # => "eirfg"
#
# cipher.decode("eta")  # => "abc"
# cipher.decode("qxz")  # => "xyz"
# cipher.decode("eirfg")  # => "aeiou"
# If
# a
# character
# provided is not in the
# opposing
# alphabet, simply
# leave
# it as be.

class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2

    def encode(self, s):
        string = ""
        for ch in s:
            string += self.map2[self.map1.index(ch)] if ch in self.map1 else ch
        return string

    def decode(self, s):
        string = ""
        for ch in s:
            string += self.map1[self.map2.index(ch)] if ch in self.map2 else ch
        return string

# Best practice:
#
#
# class Cipher(object):
#     def __init__(self, map1, map2):
#         self.enc_key = str.maketrans(map1, map2)
#         self.dec_key = str.maketrans(map2, map1)
#
#     def encode(self, stg):
#         return stg.translate(self.enc_key)
#
#     def decode(self, stg):
#         return stg.translate(self.dec_key)
#
# Clever solution:
#
# class Cipher(object):
#     def __init__(self, map1, map2):
#         self.encode_map = dict(zip(map1, map2))
#         self.decode_map = dict(zip(map2, map1))
#
#     def encode(self, string):
#         return ''.join(self.encode_map.get(c, c) for c in string)
#
#     def decode(self, string):
#         return ''.join(self.decode_map.get(c, c) for c in string)
