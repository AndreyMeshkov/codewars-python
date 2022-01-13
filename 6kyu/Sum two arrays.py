# Sum two arrays
#
# https://www.codewars.com/kata/59c3e8c9f5d5e40cab000ca6
#
# Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, and returns the sum of those two arrays.
#
# The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata, meaning it would equal 329. The output should be an array of the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). Examples are given below of what two arrays should return.
#
# [3,2,9],[1,2] --> [3,4,1]
# [4,7,3],[1,2,3] --> [5,9,6]
# [1],[5,7,6] --> [5,7,7]
# If both arrays are empty, return an empty array.
#
# In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:
#
# [3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962

def sum_arrays(array1, array2):
    if len(array1) == len(array2) == 0:
        return []
    elif len(array1) == 0:
        num = get_number(array2)
        return get_array(num)
    elif len(array2) == 0:
        num = get_number(array1)
        return get_array(num)
    else:
        num1 = get_number(array1)
        num2 = get_number(array2)
        num = num1 + num2
        return get_array(num)


def get_number(array):
    if array[0] < 0:
        array[0] = abs(array[0])
        return -int("".join([str(i) for i in array]))
    else:
        return int("".join([str(i) for i in array]))


def get_array(num):
    if num >= 0:
        return [int(i) for i in list(str(num))]
    else:
        result = [int(i) for i in list(str(-num))]
        result[0] = -result[0]
        return result

# Best practice and clever solution:
#
# def sum_arrays(array1,array2):
#     if not array1: return array2
#     if not array2: return array1
#     num = sum(map(lambda x: int(''.join(map(str, x))), [array1, array2]))
#     lst = list(map(int, str(abs(num))))
#     if num < 0: lst[0] *=-1
#     return lst