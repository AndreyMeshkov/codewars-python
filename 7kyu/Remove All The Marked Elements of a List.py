# Remove All The Marked Elements of a List
#
# https://www.codewars.com/kata/563089b9b7be03472d00002b
#
# Define a method/function that removes from a given array of integers all the values contained in a second array.
#
# Examples:
# l = List()
#
# integer_list =  [1, 1, 2 ,3 ,1 ,2 ,3 ,4]
# values_list = [1, 3]
# l.remove_(integer_list, values_list) == [2, 2, 4]
#
# integer_list = [1, 1, 2 ,3 ,1 ,2 ,3 ,4, 4, 3 ,5, 6, 7, 2, 8]
# lst = [1, 3, 4, 2]
# l.remove_(integer_list, values_list) == [5, 6 ,7 ,8]
#
# integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2 , 3]
# lst = [2, 4, 3]
# l.remove_(integer_list, values_list) == [8, 7, 6, 5, 1]
# Enjoy it!!

class List:
    def remove_(self, integer_list, values_list):
        result = []
        for n in integer_list:
            if n not in values_list:
                result.append(n)
        return result

# Best practice and clever solution:
#
# class List(object):
#     def remove_(self, integer_list, values_list):
#         blacklist = set(values_list)
#         return [val for val in integer_list if val not in blacklist]
