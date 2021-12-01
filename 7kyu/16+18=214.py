# 16+18=214
#
# https://www.codewars.com/kata/5effa412233ac3002a9e471d
#
# For this kata you will have to forget how to add two numbers.
#
# It can be best explained using the following meme: https://i.ibb.co/Y01rMJR/caf.png
#
# In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it calculates :-)
#
# You may assume both integers are positive integers.

def add(num1, num2):
    string1 = str(num1)
    string2 = str(num2)
    max_length = max(len(string1), len(string2))
    string1 = string1.rjust(max_length, "0")
    string2 = string2.rjust(max_length, "0")
    result = ""
    for i in range(len(string1)):
        result += str(int(string1[i]) + int(string2[i]))
    return int(result)

# Best practice and clever solution:
#
# def add(a,b):
#     s = ""
#     while a+b:
#         a,p = divmod(a,10)
#         b,q = divmod(b,10)
#         s = str(p+q)+s
#     return int(s or'0')