# Localize The Barycenter of a Triangle
#
# https://www.codewars.com/kata/5601c5f6ba804403c7000004
#
# source: imgur.com
# The medians of a triangle are the segments that unit the vertices with the midpoint of their opposite sides. The three medians of a triangle intersect at the same point, called the barycenter or the centroid. Given a triangle, defined by the cartesian coordinates of its vertices we need to localize its barycenter or centroid.
#
# The function bar_triang() or barTriang or bar-triang, receives the coordinates of the three vertices A, B and C as three different arguments and outputs the coordinates of the barycenter O in an array [xO, yO]
#
# This is how our asked function should work: the result of the coordinates should be expressed up to four decimals, (rounded result).
#
# You know that the coordinates of the barycenter are given by the following formulas.
#
# source: imgur.com
#
# For additional information about this important point of a triangle see at: (https://en.wikipedia.org/wiki/Centroid)
#
# Let's see some cases:
#
# bar_triang([4, 6], [12, 4], [10, 10]) ------> [8.6667, 6.6667]
#
# bar_triang([4, 2], [12, 2], [6, 10] ------> [7.3333, 4.6667]
# The given points form a real or a degenerate triangle but in each case the above formulas can be used.
#
# Enjoy it and happy coding!!

def bar_triang(pointA, pointB, pointC):
    return [round((pointA[0] + pointB[0] + pointC[0]) / 3, 4),
            round((pointA[1] + pointB[1] + pointC[1]) / 3, 4)]

# Best practice:
#
# def bar_triang((xA, yA), (xB, yB), (xC, yC)):
#     x0 = round((xA + xB + xC) / 3.0, 4)
#     y0 = round((yA + yB + yC) / 3.0, 4)
#     return [x0, y0]

# Clever solution:
#
# def bar_triang(a, b, c):
#     return [round(sum(x)/3.0, 4) for x in zip(a, b, c)]