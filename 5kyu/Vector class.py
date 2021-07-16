# # Vector class
#
# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
#
# Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
#
# a = Vector([1, 2, 3])
# b = Vector([3, 4, 5])
# c = Vector([5, 6, 7, 8])
#
# a.add(b)      # should return a new Vector([4, 6, 8])
# a.subtract(b) # should return a new Vector([-2, -2, -2])
# a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
# a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
# a.add(c)      # raises an exception
# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!
#
# Also provide:
#
# a toString method, so that using the vectors from above, a.toString() === '(1,2,3)' (in Python, this is a __str__ method, so that str(a) == '(1,2,3)')
# an equals method, to check that two vectors that have the same components are equal
# Note: the test cases will utilize the user-provided equals method.

class Vector:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def add(self, vector):
        if len(vector.coordinates) != len(self.coordinates):
            raise Exception("Error")
        new_coordinates = []
        for i in range(0, len(vector.coordinates)):
            new_coordinates.append(vector.coordinates[i] + self.coordinates[i])
        return Vector(new_coordinates)

    def subtract(self, vector):
        if len(vector.coordinates) != len(self.coordinates):
            raise Exception("Error")
        new_coordinates = []
        for i in range(0, len(vector.coordinates)):
            new_coordinates.append(self.coordinates[i] - vector.coordinates[i])
        return Vector(new_coordinates)

    def dot(self, vector):
        if len(vector.coordinates) != len(self.coordinates):
            raise Exception("Error")
        new_coordinates = []
        for i in range(0, len(vector.coordinates)):
            new_coordinates.append(self.coordinates[i] * vector.coordinates[i])
        return sum(new_coordinates)

    def norm(self):
        return sum([x ** 2 for x in self.coordinates]) ** 0.5

    def __str__(self):
        return str(tuple(self.coordinates)).replace(" ", "")

    def equals(self, other):
        if isinstance(other, Vector):
            for i in range(0, len(self.coordinates)):
                if self.coordinates[i] != other.coordinates[i]:
                    return False
        return True

# Best practice and clever solution:
#
# from math import sqrt
# import operator as op
# from itertools import imap
#
#
# class Vector:
#     # TODO: Finish the Vector class.
#     def __init__(self, array=[]):
#         self.__data = array
#
#     def __len__(self):
#         return len(self.__data)
#
#     def __iter__(self):
#         return iter(self.__data)
#
#     def __getitem__(self, i):
#         return self.__data[i]
#
#     def check_length(f):
#         def wrapper(self, other):
#             if len(self) != len(other):
#                 raise ValueError()
#             return f(self, other)
#
#         return wrapper
#
#     @check_length
#     def add(self, other):
#         res = Vector(map(op.add, self, other))
#         return res
#
#     @check_length
#     def subtract(self, other):
#         res = Vector(map(op.sub, self, other))
#         return res
#
#     @check_length
#     def dot(self, other):
#         res = reduce(op.add, imap(op.mul, self, other))
#         return res
#
#     def norm(self):
#         return sqrt(self.dot(self))
#
#     def equals(self, other):
#         if len(self) != len(other):
#             return False
#         return all(map(op.eq, self, other))
#
#     def __str__(self):
#         return '(%s)' % ','.join(str(x) for x in self.__data)
