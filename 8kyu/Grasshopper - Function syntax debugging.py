# Grasshopper - Function syntax debugging
#
# https://www.codewars.com/kata/56dae9dc54c0acd29d00109a
#
# Grasshopper - Function syntax debugging
# A student was working on a function and made some syntax mistakes while coding. Help them find their mistakes and fix them.

def main(verb, noun):
    return verb + noun

# Best practice:
#
# def main(verb, noun):
#     return verb + noun

# Clever solution:
#
# def main(*a):
#     return ''.join(a)
