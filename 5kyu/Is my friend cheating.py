# Is my friend cheating?
#
# https://www.codewars.com/kata/5547cc7dcad755e480000004
#
# A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
# Given a number n, could you tell me the numbers he excluded from the sequence?
# The function takes the parameter: n (n is always strictly greater than 0) and returns an array or a string (depending on the language) of the form:
#
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or or [{a, b}, ...]
# with all (a, b) which are the possible removed numbers in the sequence 1 to n.
#
# [(a, b), ...] or [[a, b], ...] or {{a, b}, ...} or ... will be sorted in increasing order of the "a".
#
# It happens that there are several possible (a, b). The function returns an empty array (or an empty string) if no possible numbers are found which will prove that my friend has not told the truth! (Go: in this case return nil).
#
# Examples:
# removNb(26) should return [(15, 21), (21, 15)]
# or
# removNb(26) should return { {15, 21}, {21, 15} }
# or
# removeNb(26) should return [[15, 21], [21, 15]]
# or
# removNb(26) should return [ {15, 21}, {21, 15} ]
# or
# removNb(26) should return "15 21, 21 15"
# or
#
# in C:
# removNb(26) should return  {{15, 21}{21, 15}} tested by way of strings.
# Function removNb should return a pointer to an allocated array of Pair pointers, each one also allocated.
# Note
# See examples of returns for each language in "RUN SAMPLE TESTS"

def removNb(n):
    result = []
    sequence_sum = n * (n + 1) // 2
    for x in range(1, n + 1):
        y = (sequence_sum - x) // (x + 1)
        if y <= n and x * y == (sequence_sum - x - y):
            result.append((x, y))
    return result

# Best practice:
#
# def removNb(n):
#     total = n*(n+1)/2
#     sol = []
#     for a in range(1,n+1):
#         b = (total-a)/(a+1.0)
#         if b.is_integer() and b <= n:
#             sol.append((a,int(b)))
#     return sol

# Clever solution:
#
# def removNb(n):
#     sum = n*(n + 1)/2
#     return [(x, (sum - x) / (x + 1)) for x in xrange(1, n+1) if (sum - x) % (x + 1) == 0 and 1 <= (sum - x) / (x + 1) <= n]
