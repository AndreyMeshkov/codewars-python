# Even or Odd - Which is Greater?
#
# https://www.codewars.com/kata/57f7b8271e3d9283300000b4
#
# Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.
#
# If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"
#
# If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"
#
# If the total of both even and odd numbers are identical return: "Even and Odd are the same"

def even_or_odd(s):
    numbers = list(s)
    odd_sum = sum(int(i) for i in numbers if int(i) % 2)
    even_sum = sum(int(i) for i in numbers if int(i) % 2 == 0)
    if odd_sum == even_sum:
        return 'Even and Odd are the same'
    elif odd_sum > even_sum:
        return 'Odd is greater than Even'
    else:
        return 'Even is greater than Odd'

# Best practice and clever solution:
#
# def even_or_odd(s):
#     even_minus_odd = sum([-x if x % 2 else x for x in map(int, s)])
#     if even_minus_odd > 0:
#         return "Even is greater than Odd"
#     elif even_minus_odd < 0:
#         return "Odd is greater than Even"
#     else:
#         return "Even and Odd are the same"
