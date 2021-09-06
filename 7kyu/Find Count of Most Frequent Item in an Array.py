# Find Count of Most Frequent Item in an Array
#
# https://www.codewars.com/kata/56582133c932d8239900002e
#
# Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
#
# Example
# input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
# ouptut: 5
# The most frequent number in the array is -1 and it occurs 5 times.

def most_frequent_item_count(collection):
    result = 0
    for num in collection:
        if collection.count(num) > result:
            result = collection.count(num)
    return result

# Best practice and clever solution:
#
# def most_frequent_item_count(collection):
#     if collection:
#         return max([collection.count(item) for item in collection])
#     return 0