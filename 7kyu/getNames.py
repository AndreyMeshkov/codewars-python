# getNames()
#
# https://www.codewars.com/kata/514a677421607afc99000002
#
# The following code is not giving the expected results. Can you debug what the issue is?
#
# The following is an example of data that would be passed in to the function.
#
# data = [
#     {'name': 'Joe', 'age': 20},
#     {'name': 'Bill', 'age': 30},
#     {'name': 'Kate', 'age': 23}
# ]
# get_names(data) # should return ['Joe', 'Bill', 'Kate']

def itemgetter(item):
    return item['name']


def get_names(data):
    return list(map(itemgetter, data))

# Best practice and clever solution:
#
#
# def itemgetter(item):
#     return item['name']
#
#
# def get_names(data):
#     return list(map(itemgetter, data))
