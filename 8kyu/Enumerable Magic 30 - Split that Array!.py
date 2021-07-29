# Enumerable Magic #30 - Split that Array!
#
# https://www.codewars.com/kata/545b342082e55dc9da000051
#
# Create a method partition that accepts a list and a method/block. It should return two arrays: the first, with all the elements for which the given block returned true, and the second for the remaining elements.
#
# Here's a simple Ruby example:
#
# animals = ["cat", "dog", "duck", "cow", "donkey"]
# partition(animals){|animal| animal.size == 3}
#     #=> [["cat", "dog", "cow"], ["duck", "donkey"]]
# The equivalent in Python would be:
#
# animals = ['cat', 'dog', 'duck', 'cow', 'donkey']
# partition(animals, lambda x: len(x) == 3)
#     # (['cat', 'dog', 'cow'], ['duck', 'donkey'])
# If you need help, here's a reference:
#
# http://www.rubycuts.com/enum-partition

def partition(arr, classifier_method):
    first_list = []
    second_list = []
    for i in arr:
        if classifier_method(i):
            first_list.append(i)
        else:
            second_list.append(i)

    return (first_list, second_list)

# Best practice:
#
# from itertools import filterfalse
# def partition(lis, classifier_method):
#     fir = list(filter(classifier_method, lis))
#     sec = list(filterfalse(classifier_method, lis))
#     return (fir, sec)

# Clever solution:
#
# def partition(list, m):
#     return ([x for x in list if m(x)],[x for x in list if not m(x)])