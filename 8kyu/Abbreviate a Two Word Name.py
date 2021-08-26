# Abbreviate a Two Word Name
#
# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3
#
# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
#
# The output should be two capital letters with a dot separating them.
#
# It should look like this:
#
# Sam Harris => S.H
#
# Patrick Feeney => P.F

def abbrev_name(name):
    return f'{name.split(" ")[0][0].upper()}.{name.split(" ")[1][0].upper()}'

# Best practice and clever solution:
#
# def abbrevName(name):
#     return '.'.join(w[0] for w in name.split()).upper()
