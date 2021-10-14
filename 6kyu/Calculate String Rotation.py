# Calculate String Rotation
#
# https://www.codewars.com/kata/5596f6e9529e9ab6fb000014
#
# Write a function that receives two strings and returns n, where n is equal to the number of characters we should shift the first string forward to match the second. The check should be case sensitive.
#
# For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 5 characters forward to produce the second string, so 5 would be returned.
#
# If the second string isn't a valid rotation of the first string, the method returns -1.
# Examples:
# "coffee", "eecoff" => 2
# "eecoff", "coffee" => 4
# "moose", "Moose" => -1
# "isn't", "'tisn" => 2
# "Esham", "Esham" => 0
# "dog", "god" => -1

def shifted_diff(first, second, count=0):
    if first == second:
        return count
    if count > len(first):
        return -1
    return shifted_diff(first[-1] + first[0:-1], second, count + 1)

# Best practice and clever solution:
#
# def shifted_diff(first, second):
#     return (second + second).find(first) if len(first) == len(second) else - 1;
