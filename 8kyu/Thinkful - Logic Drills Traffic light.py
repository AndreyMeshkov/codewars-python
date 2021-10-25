# Thinkful - Logic Drills: Traffic light
#
# https://www.codewars.com/kata/58649884a1659ed6cb000072
#
# You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.
#
# Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.
#
# For example, update_light('green') should return 'yellow'.
#
# Note: Use "" instead of '' in C++.

def update_light(current):
    colors = ["green", "yellow", "red"]
    return colors[(colors.index(current) + 1) % 3]

# Best practice and clever solution:
#
# def update_light(current):
#     return {"green": "yellow", "yellow": "red", "red": "green"}[current]
