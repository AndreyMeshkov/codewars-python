# Calculate BMI
#
# https://www.codewars.com/kata/57a429e253ba3381850000fb
#
# Write function bmi that calculates body mass index (bmi = weight / height2).
#
# if bmi <= 18.5 return "Underweight"
#
# if bmi <= 25.0 return "Normal"
#
# if bmi <= 30.0 return "Overweight"
#
# if bmi > 30 return "Obese"

def bmi(weight, height):
    result = weight / height ** 2
    if result <= 18.5:
        return "Underweight"
    elif result <= 25:
        return "Normal"
    elif result <= 30:
        return "Overweight"
    elif result > 30:
        return "Obese"

# Best practice:
#
# def bmi(weight, height):
#     bmi = weight / height ** 2
#     if bmi <= 18.5:
#         return "Underweight"
#     elif bmi <= 25:
#         return "Normal"
#     elif bmi <= 30:
#         return "Overweight"
#     else:
#         return "Obese"

# Clever solution:
#
# def bmi(weight, height):
#     b = weight / height ** 2
#     return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]
