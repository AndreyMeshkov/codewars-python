# Chuck Norris VII - True or False? (Beginner)
#
# https://www.codewars.com/kata/570669d8cb7293a2d1001473
#
# It's a well known fact that anything Chuck Norris wants, he gets. As a result Chuck very rarely has to use the word false.
#
# It is a less well known fact that if something is true, and Chuck doesn't want it to be, Chuck can scare the truth with his massive biceps, and it automatically becomes false.
#
# Your task is to be more like Chuck (ha! good luck!). You must return false without ever actually using the word false...
#
# Go show some truth who's boss!

def ifChuckSaysSo():
    return not True

# Best practice:
#
# def ifChuckSaysSo():
#     return 0
#
# Clever solution:
#
# def ifChuckSaysSo():
#     this_kata_sucks = True
#     return this_kata_sucks - 1
