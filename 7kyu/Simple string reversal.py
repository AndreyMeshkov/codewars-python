# Simple string reversal
#
# https://www.codewars.com/kata/5a71939d373c2e634200008e
#
# In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.
#
# For example:
#
# solve("our code") = "edo cruo"
# -- Normal reversal without spaces is "edocruo".
# -- However, there is a space at index 3, so the string becomes "edo cruo"
#
# solve("your code rocks") = "skco redo cruoy".
# solve("codewars") = "srawedoc"
# More examples in the test cases. All input will be lower case letters and in some cases spaces.
#
# Good luck!
#
# Please also try:
#
# Simple time difference
#
# Simple remove duplicates

def solve(s):
    string = s.replace(" ", "")[::-1]
    for i in range(len(s)):
        if s[i] == " ":
            string = string[0:i] + " " + string[i:]
    return string

# Best practice and clever solution:
#
# def solve(s):
#     it = reversed(s.replace(' ',''))
#     return ''.join(c if c == ' ' else next(it) for c in s)