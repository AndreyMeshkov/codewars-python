# Multiply the number
#
# codewars.com/kata/5708f682c69b48047b000e07
#
# Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:
#
# multiply(3)==15
# multiply(10)==250
# multiply(200)==25000
# multiply(0)==0
# multiply(-3)==-15

def multiply(n):
    return n * (5 ** len(str(n))) if n > 0 else n * (5 ** len(str(-n)))

# Best practice and clever solution:
#
# def multiply(n):
#   return n*5**len(str(abs(n)))
