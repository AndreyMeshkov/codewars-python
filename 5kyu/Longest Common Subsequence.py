# Longest Common Subsequence
#
# https://www.codewars.com/kata/52756e5ad454534f220001ef
#
# Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.
#
# Subsequence
# A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.
#
# Example subsequence
# Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".
#
# LCS examples
# lcs( "abcdef" , "abc" ) => returns "abc"
# lcs( "abcdef" , "acf" ) => returns "acf"
# lcs( "132535365" , "123456789" ) => returns "12356"
# Notes
# Both arguments will be strings
# Return value must be a string
# Return an empty string if there exists no common subsequence
# Both arguments will have one or more characters (in JavaScript)
# All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ), which would have two possible longest common subsequences: "12" and "34".
# Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.
#
# Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest common subsequence will be valid).
#
# Tips
# Wikipedia has an explanation of the two properties that can be used to solve the problem:
#
# First property
# Second property

def lcs(x, y):
    n = len(x)
    m = len(y)
    L = [[0 for j in range(m + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
    result = ""
    i = n
    j = m
    while L[i][j] > 0:
        if L[i][j] == L[i][j - 1]:
            j -= 1
        elif L[i][j] == L[i - 1][j]:
            i -= 1
        else:
            result = x[i - 1] + result
            i -= 1
            j -= 1
    return result

# Best practice:
#
# def lcs(x, y):
#     if len(x) == 0 or len(y) == 0:
#         return ''
#     if x[-1] == y[-1]:
#         return lcs(x[:-1], y[:-1]) + x[-1]
#     else:
#         lcs1 = lcs(x,y[:-1])
#         lcs2 = lcs(x[:-1],y)
#         if len(lcs1) > len(lcs2):
#             return lcs1
#         else:
#             return lcs2

# Clever solution:
#
# from itertools import combinations
#
# def subsequences(s):
#     """Returns set of all subsequences in s."""
#     return set(''.join(c) for i in range(len(s) + 1) for c in combinations(s, i))
#
# def lcs(x, y):
#     """Returns longest matching subsequence of two strings."""
#     return max(subsequences(x).intersection(subsequences(y)), key=len)