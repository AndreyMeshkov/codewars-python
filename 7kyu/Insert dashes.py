# Insert dashes
#
# https://www.codewars.com/kata/55960bbb182094bc4800007b
#
# Write a function insert_dash(num) / insertDash(num) / InsertDash(int num) that will insert dashes ('-') between each two odd digits in num. For example: if num is 454793 the output should be 4547-9-3. Don't count zero as an odd digit.
#
# Note that the number will always be non-negative (>= 0).

def insert_dash(num):
    result = ""
    string = str(num)
    for i in range(1, len(string)):
        if int(string[i - 1]) % 2 and int(string[i]) % 2:
            result += string[i - 1] + "-"
        else:
            result += string[i - 1]
    return result + string[-1]

# Best practice and clever solution:
#
# import re
#
# def insert_dash(num):
#     #your code here
#     return re.sub(r'([13579])(?=[13579])', r'\1-', str(num))
