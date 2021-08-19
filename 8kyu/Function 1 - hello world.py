# Function 1 - hello world
#
# https://www.codewars.com/kata/523b4ff7adca849afe000035
#
# Description:
# Make a simple function called greet that returns the most-famous "hello world!".
#
# Style Points
# Sure, this is about as easy as it gets. But how clever can you be to create the most creative hello world you can think of? What is a "hello world" solution you would want to show your friends?

def greet():
    return "hello world!"

# Best practice:
#
# def greet():
#     return "hello world!"

# Clever solution:
#
# from subprocess import check_output
# greet = lambda: check_output(["python3", "-c", "import __hello__"]).decode('ascii').lower()[:-1]