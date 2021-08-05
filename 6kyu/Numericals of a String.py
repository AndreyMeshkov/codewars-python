# Numericals of a String
#
# https://www.codewars.com/kata/5b4070144d7d8bbfe7000001
#
# You are given an input string.
#
# For each symbol in the string if it's the first character occurrence, replace it with a '1', else replace it with the amount of times you've already seen it.
#
# Examples:
# input   =  "Hello, World!"
# result  =  "1112111121311"
#
# input   =  "aaaaaaaaaaaa"
# result  =  "123456789101112"
# There might be some non-ascii characters in the string.
#
# Take note of performance

def numericals(s):
    result = ""
    dict = {}
    for i in range(len(s)):
        if s[i] in dict.keys():
            dict[s[i]] += 1
        else:
            dict[s[i]] = 1
        result += str(dict[s[i]])
    return result

# Best practice:
#
# def numericals(s):
#     dictio = {}
#     t = ""
#     for i in s:
#         dictio[i] = dictio.get(i,0) + 1
#         t += str(dictio[i])
#     return t

# Clever solution:
#
# from collections import defaultdict
#
# def numericals(s):
#     d = defaultdict(int)
#     return ''.join(map(str, (d[c] for c in s if d.__setitem__(c,d[c]+1) or 1) ))
