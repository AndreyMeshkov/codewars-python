# Counting sheep...
#
# https://www.codewars.com/kata/54edbc7200b811e956000556
#
# Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
#
# For example,
#
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
#
# Hint: Don't forget to check for bad values like null/undefined

def count_sheeps(sheep):
    result = 0
    for i in sheep:
        if i == True:
            result += 1
    return result

# Best practice and clever solution:
#
# def count_sheeps(arrayOfSheeps):
#   return arrayOfSheeps.count(True)
