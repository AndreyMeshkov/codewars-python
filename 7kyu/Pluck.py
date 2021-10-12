# Pluck
#
# https://www.codewars.com/kata/530017aac7c0f49926000084
#
# Implement a function which takes a sequence of objects and a property name, and returns a sequence containing the named property of each object.
#
# For example:
#
# pluck([{'a':1}, {'a':2}], 'a')        # -> [1,2]
# pluck([{'a':1, 'b':3}, {'a':2}], 'b') # -> [3, None]
# If an object is missing the property, you should just leave it as undefined/None in the output array.


def pluck(objs, name):
    result = []
    for obj in objs:
        if name in obj:
            result.append(obj[name])
        else:
            result.append(None)
    return result

# Best practiec and clever solution:
#
# def pluck(objs, name):
#     return [item.get(name) for item in objs]
