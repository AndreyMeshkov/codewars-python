# Age Range Compatibility Equation
#
# https://www.codewars.com/kata/5803956ddb07c5c74200144e
#
# Everybody knows the classic "half your age plus seven" dating rule that a lot of people follow (including myself). It's the 'recommended' age range in which to date someone.
#
#
# minimum age <= your age <= maximum age #Task
#
# Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.
#
# This equation doesn't work when the age <= 14, so use this equation instead:
#
# min = age - 0.10 * age
# max = age + 0.10 * age
# You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form [min]-[max]
#
# ##Examples:
#
# age = 27   =>   20-40
# age = 5    =>   4-5
# age = 17   =>   15-20

def dating_range(age):
    return f"{int(age / 2) + 7}-{(age - 7) * 2}" if age > 14 else f"{int(age * 0.9)}-{int(age * 1.1)}"

# Best practice:
#
# def dating_range(age):
#     if age <= 14:
#         min = age - 0.10 * age
#         max = age + 0.10 * age
#     else:
#         min = (age / 2) + 7
#         max = (age - 7) * 2
#
#     return str(int(min)) + '-' + str(int(max))
# Clever solution:
#
# def dating_range(age):
#     return ['%d-%d'%(age-.10*age, age+.10*age), '%d-%d'%(age/2+7, (age-7)*2)][age>14]
