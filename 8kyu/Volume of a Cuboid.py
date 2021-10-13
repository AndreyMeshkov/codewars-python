# Volume of a Cuboid
#
# https://www.codewars.com/kata/58261acb22be6e2ed800003a
#
# Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid. Write a function to help Bob with this calculation.

def getVolumeOfCubiod(length, width, height):
    return length * width * height

# Best practice:
#
# def get_volume_of_cuboid(length, width, height):
#     return length * width * height
#
#
# # PEP8: kata function name should use snake_case not mixedCase
# getVolumeOfCubiod = get_volume_of_cuboid

# Clever solution:
#
# def getVolumeOfCubiod(l, w, h):
#     return l * w * h
