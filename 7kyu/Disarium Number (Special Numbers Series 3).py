# Disarium Number (Special Numbers Series #3)
#
# https://www.codewars.com/kata/5a53a17bfd56cb9c14000003
#
# Definition
# Disarium number is the number that The sum of its digits powered with their respective positions is equal to the number itself.
#
# Task
# Given a number, Find if it is Disarium or not .
#
# Warm-up (Highly recommended)
# Playing With Numbers Series
# Notes
# Number passed is always Positive .
# Return the result as String
# Input >> Output Examples
# disariumNumber(89) ==> return "Disarium !!"
# Explanation:
# Since , 81 + 92 = 89 , thus output is "Disarium !!"
# disariumNumber(564) ==> return "Not !!"
# Explanation:
# Since , 51 + 62 + 43 = 105 != 564 , thus output is "Not !!"

def disarium_number(number):
    string = str(number)
    return "Disarium !!" if sum([int(string[i]) ** (i + 1) for i in
                                 range(len(string))]) == number else "Not !!"

# Best practice and clever solution:
#
# def disarium_number(n):
#     return "Disarium !!" if n == sum(int(d)**i for i, d in enumerate(str(n), 1)) else "Not !!"
