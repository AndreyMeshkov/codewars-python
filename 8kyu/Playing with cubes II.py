# Playing with cubes II
#
# https: // www.codewars.com / kata / 55c0ac142326fdf18d0000af
#
# Hey Codewarrior!
#
# You already implemented a Cube class, but now we need your help again! I'm talking about constructors. We don't have one. Let's code two: One taking an integer and one handling no given arguments!
#
# Also we got a problem with negative values. Correct the code so negative values will be switched to positive ones!
#
# The constructor taking no arguments should assign 0 to Cube's Side property.

class Cube(object):
    def __init__(self, side=0):
        self._side = side

    def get_side(self):
        return self._side

    def set_side(self, new_side):
        if new_side < 0:
            new_side *= -1
        self._side = new_side

# Best practice and clever solution:
#
# class Cube:
#     def __init__(self, side=0):
#         self._side = side
#
#     def get_side(self):
#         return self._side
#
#     def set_side(self, new_side):
#         self._side = abs(new_side)
