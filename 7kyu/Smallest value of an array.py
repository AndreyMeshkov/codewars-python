# Smallest value of an array
#
# https://www.codewars.com/kata/544a54fd18b8e06d240005c0
#
# Write a function that can return the smallest value of an array or the index of that value. The function's 2nd parameter will tell whether it should return the value or the index.
#
# Assume the first parameter will always be an array filled with at least 1 number and no duplicates. Assume the second parameter will be a string holding one of two values: 'value' and 'index'.
#
# min([1,2,3,4,5], 'value') // => 1
# min([1,2,3,4,5], 'index') // => 0

def find_smallest(numbers, to_return):
    if to_return == "value":
        return min(numbers)
    elif to_return == "index":
        return numbers.index(min(numbers))

# Best practice:
#
# def find_smallest(numbers,to_return):
#     return min(numbers) if to_return == 'value' else numbers.index(min(numbers))
#
# Clever solution:
#
# find_smallest = lambda n,t: [n.index, lambda x:x][t[0]=='v'](min(n))
