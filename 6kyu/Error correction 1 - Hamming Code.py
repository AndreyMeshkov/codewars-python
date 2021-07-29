# Error correction #1 - Hamming Code
#
# https://www.codewars.com/kata/5ef9ca8b76be6d001d5e1c3e
#
# Translations appreciated
#
# Background information
# The Hamming Code is used to correct errors, so-called bit flips, in data transmissions. Later in the description follows a detailed explanation of how it works.
# In this Kata we will implement the Hamming Code with bit length 3; this has some advantages and disadvantages:
#
# [ + ] It's simple to implement
# [ + ] Compared to other versions of hamming code, we can correct more mistakes
# [ - ] The size of the input triples
# Task 1: Encode function
# Implement the encode function, using the following steps:
#
# convert every letter of the text to its ASCII value;
# convert ASCII values to 8-bit binary;
# triple every bit;
# concatenate the result;
# For example:
#
# input: "hey"
# --> 104, 101, 121                  // ASCII values
# --> 01101000, 01100101, 01111001   // binary
# --> 000111111000111000000000 000111111000000111000111 000111111111111000000111  // tripled
# --> "000111111000111000000000000111111000000111000111000111111111111000000111"  // concatenated
# Task 2: Decode function:
# Check if any errors happened and correct them. Errors will be only bit flips, and not a loss of bits:
#
# 111 --> 101 : this can and will happen
# 111 --> 11 : this cannot happen
# Note: the length of the input string is also always divisible by 24 so that you can convert it to an ASCII value.
#
# Steps:
#
# Split the input into groups of three characters;
# Check if an error occurred: replace each group with the character that occurs most often, e.g. 010 --> 0, 110 --> 1, etc;
# Take each group of 8 characters and convert that binary number;
# Convert the binary values to decimal (ASCII);
# Convert the ASCII values to characters and concatenate the result
# For example:
#
# input: "100111111000111001000010000111111000000111001111000111110110111000010111"
# --> 100, 111, 111, 000, 111, 001, ...  // triples
# -->  0,   1,   1,   0,   1,   0,  ...  // corrected bits
# --> 01101000, 01100101, 01111001       // bytes
# --> 104, 101, 121                      // ASCII values
# --> "hey"
# If you liked this kata, please try out some of my other katas:
# Crack the PIN
# Decode the QR-Code
# Hack the NSA

def encode(string):
    result = ""
    ascii_list = [ord(ch) for ch in string]
    binary_list = [bin(i).replace("0b", "") for i in ascii_list]
    binary_list = ["0" * (- len(i) % 8) + i for i in binary_list]
    tripled_list = []
    for i in binary_list:
        tripled_i = ""
        for ch in i:
            tripled_i += ch * 3
        tripled_list.append(tripled_i)
    for i in tripled_list:
        result += i
    return result


def decode(bits):
    triples_list = []
    for i in range(0, len(bits), 3):
        triples_list.append(bits[i:i + 3])
    corrected_bits_list = []
    for i in triples_list:
        if i.count("1") > 1:
            corrected_bits_list.append("1")
        else:
            corrected_bits_list.append("0")
    bytes_list = []
    for i in range(0, len(corrected_bits_list), 8):
        bytes_list.append("".join(corrected_bits_list[i: i + 8]))
    ascii_list = [int(i, 2) for i in bytes_list]
    letters = [chr(i) for i in ascii_list]
    return "".join(letters)

# Best practice:
#
#
# def encode(stg):
#     return "".join(digit * 3 for char in stg for digit in f"{ord(char):08b}")
#
#
# def decode(binary):
#     reduced = (get_digit(triplet) for triplet in chunks(binary, 3))
#     return "".join(get_char(byte) for byte in chunks("".join(reduced), 8))
#
#
# def chunks(seq, size):
#     return (seq[i:i + size] for i in range(0, len(seq), size))
#
#
# def get_digit(triplet):
#     return max(triplet, key=triplet.count)
#
#
# def get_char(byte):
#     return chr(int(byte, 2))

# Clever solution:
#
# def encode(uncoded):
#     encoded = ''.join(''.join(b * 3 for b in bin(ord(c))[2:].zfill(8)) for c in uncoded)
#     return encoded
#
# def decode(encoded):
#     patches = {'000':'0','001':'0','010':'0','100':'0','011':'1','101':'1','110':'1','111':'1'}
#     patched = ''.join(patches[encoded[i:i + 3]] for i in range(0, len(encoded), 3))
#     decoded = ''.join(chr(int(patched[i:i + 8], 2)) for i in range(0, len(patched), 8))
#     return decoded
