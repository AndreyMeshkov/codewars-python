# Grasshopper - Debug sayHello
#
# https://www.codewars.com/kata/5625618b1fe21ab49f00001f
#
# Debugging sayHello function
# The starship Enterprise has run into some problem when creating a program to greet everyone as they come aboard. It is your job to fix the code and get the program working again!
#
# Example output:
#
# Hello, Mr. Spock

def say_hello(name):
    return f"Hello, {name}"

# Best practice:
#
# def say_hello(name):
#     return f"Hello, {name}"
#
# Clever solution:
#
# say_hello = "Hello, ".__add__
