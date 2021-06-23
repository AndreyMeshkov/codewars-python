# Custom FizzBuzz Array
#
# https://www.codewars.com/kata/5355a811a93a501adf000ab7
#
# Write a function that returns a (custom) FizzBuzz sequence of the numbers 1 to 100.
#
# The function should be able to take up to 4 arguments:
#
# The 1st and 2nd arguments are strings, "Fizz" and "Buzz" by default;
# The 3rd and 4th arguments are integers, 3 and 5 by default.
# Thus, when the function is called without arguments, it will return the classic FizzBuzz sequence up to 100:
#
# [ 1, 2, "Fizz", 4, "Buzz", "Fizz", 7, ... 14, "FizzBuzz", 16, 17, ... 98, "Fizz", "Buzz" ]
# When the function is called with (up to 4) arguments, it should return a custom FizzBuzz sequence, for example:
#
# ('Hey', 'There')      -->  [ 1, 2, "Hey", 4, "There", "Hey", ... ]
# ('Foo', 'Bar', 2, 3)  -->  [ 1, "Foo", "Bar", "Foo", 5, "FooBar", 7, ... ]
# Examples
# fizz_buzz_custom()[15]                         # returns 16
# fizz_buzz_custom()[44]                         # returns "FizzBuzz" (45 is divisible by 3 and 5)
# fizz_buzz_custom('Hey', 'There')[25]         # returns 26
# fizz_buzz_custom('Hey', 'There')[11]         # returns "Hey" (12 is divisible by 3)
# fizz_buzz_custom("What's ", "up?", 3, 7)[80] # returns "What's " (81 is divisible by 3)
# The function must return the sequence as a list.

def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5):
    result = []
    for i in range(1,101):
        if i % num_one==0 and i % num_two==0:
            result.append(string_one + string_two)
        elif i % num_one == 0:
            result.append(string_one)
        elif i % num_two == 0:
            result.append(string_two)
        else:
            result.append(i)
    return result

# Best practice:
#
# def fizz_buzz_custom(string_one="Fizz", string_two="Buzz", num_one=3, num_two=5):
#     result = []
#     for i in range(1, 101):
#         x = ""
#         if i % num_one == 0:
#             x += string_one
#         if i % num_two == 0:
#             x += string_two
#         result.append(x or i)
#     return result

# Clever solution:
#
# def fizz_buzz_custom(a="Fizz", b="Buzz", c=3, d=5):
#     return [a * (not i % c) + b * (not i % d) or i for i in range(1, 101)]
