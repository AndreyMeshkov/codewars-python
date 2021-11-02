# Naughty or Nice?
#
# https://www.codewars.com/kata/52a6b34e43c2484ac10000cd/train/python
#
# Happy Holidays fellow Code Warriors!
# It's almost Christmas! That means Santa's making his list, and checking it twice. Unfortunately, elves accidentally mixed the Naughty and Nice list together! Santa needs your help to save Christmas!
#
# Save Christmas!
# Santa needs you to write two functions. Both of the functions accept a sequence of objects. The first one returns a sequence containing only the names of the nice people, and the other returns a sequence containing only the names of the naughty people. Return an empty sequence [] if the result from either of the functions contains no names.
#
# The objects in the passed will represent people. Each object contains two properties: name and wasNice.
# name - The name of the person
# wasNice - True if the person was nice this year, false if they were naughty
#
# Person Object Examples
# Test Examples
# get_nice_names( [
#     { 'name': 'Warrior reading this kata', 'was_nice': True },
#     { 'name': 'xDranik', 'was_nice': False },
#     { 'name': 'Santa', 'was_nice': True }
# ] )
# # => returns [ 'Warrior reading this kata', 'Santa' ]

def get_nice_names(people):
    return [person["name"] for person in people if person["was_nice"]]


def get_naughty_names(people):
    return [person["name"] for person in people if not person["was_nice"]]

# Best practice:
#
# def get_nice_names(people):
#     return [p['name'] for p in people if p['was_nice']]
#
# def get_naughty_names(people):
#     return [p['name'] for p in people if not p['was_nice']]

# Clever solution:
#
# def get_names(was_nice):
#     return lambda people: [p['name'] for p in people if p['was_nice'] == was_nice]
#
# get_nice_names = get_names(True)
# get_naughty_names = get_names(False)
