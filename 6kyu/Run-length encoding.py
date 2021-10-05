# Run-length encoding
#
# https://www.codewars.com/kata/546dba39fa8da224e8000467
#
# Run-length encoding (RLE) is a very simple form of data compression in which runs of data (that is, suences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. Wikipedia
#
# Task
# Your task is to write such a run-length encoding. For a given string, return a list (or array) of pairs (or arrays) [ (i1, s1), (i2, s2), …, (in, sn) ], such that one can reconstruct the original string by replicating the chacter sx ix times and concatening all those strings. Your run-length encoding should be minimal, ie. for all i the values si and si+1 should differ.
#
# Examples
# As the article states, RLE is a very simple form of data compression. It's only suitable for runs of data, as one can see in the following example:
#
# run_length_encoding("hello world!")
#  //=>      [[1,'h'], [1,'e'], [2,'l'], [1,'o'], [1,' '], [1,'w'], [1,'o'], [1,'r'], [1,'l'], [1,'d'], [1,'!']]
# It's very effective if the same data value occurs in many consecutive data elements:
#
# run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")
# # => [[34,'a'], [3,'b']]

def run_length_encoding(s):
    if len(s) == 0:
        return []
    result = []
    count = 1
    ch = s[0]
    for i in range(1, len(s)):
        if s[i] == ch:
            count = count + 1
        else:
            result.append([count, ch])
            ch = s[i]
            count = 1
    result.append([count, ch])
    return result

# Best practice and clever solution:
#
# from itertools import groupby
#
# def run_length_encoding(s):
#     return [[sum(1 for _ in g), c] for c, g in groupby(s)]