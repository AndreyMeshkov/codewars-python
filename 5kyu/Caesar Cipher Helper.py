# Caesar Cipher Helper
#
# https://www.codewars.com/kata/526d42b6526963598d0004db
#
# Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.
#
# For example:
#
# c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# c.encode('Codewars') # returns 'HTIJBFWX'
# c.decode('BFKKQJX') # returns 'WAFFLES'
# If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
# The shift will always be in range of [1, 26].

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encode(self, st):
        result = ""
        for i in st:
            if i.upper() in self.alphabet:
                result += self.alphabet[
                    (self.alphabet.index(i.upper()) + self.shift) % 26]
            else:
                result += i
        return result

    def decode(self, st):
        result = ""
        for i in st:
            if i.upper() in self.alphabet:
                result += self.alphabet[
                    (self.alphabet.index(i.upper()) - self.shift + 26) % 26]
            else:
                result += i
        return result

# Best practice and clever solution:
#
# from string import maketrans
#
#
# class CaesarCipher(object):
#
#     def __init__(self, shift):
#         self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
#         self.newalpha = self.alpha[shift:] + self.alpha[:shift]
#
#     def encode(self, str):
#         t = maketrans(self.alpha, self.newalpha)
#         return str.upper().translate(t)
#
#     def decode(self, str):
#         t = maketrans(self.newalpha, self.alpha)
#         return str.upper().translate(t)