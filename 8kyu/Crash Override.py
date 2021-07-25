# Crash Override
#
# https://www.codewars.com/kata/578c1e2edaa01a9a02000b7f
#
# Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable examples from the film Hackers.
#
# Your task is to create a function that, given a proper first and last name, will return the correct alias.
#
# Two objects that return a one word name in response to the first letter of the first name and one for the first letter of the surname are already given.
#
# If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your name must start with a letter from A - Z."
#
# Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for these grammatical errors.
#
# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}
#
# alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
# alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
# Happy hacking!

def alias_gen(f_name, l_name):
    if f_name[0].isdigit() or l_name[0].isdigit():
        return 'Your name must start with a letter from A - Z.'
    return f"{FIRST_NAME[f_name[0].upper()]} {SURNAME[l_name[0].upper()]}"

# Best practice:
#
# def alias_gen(f_name, l_name):
#     try:
#         return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
#     except:
#         return 'Your name must start with a letter from A - Z.'
#
# Clever solution:
#
# def alias_gen(f_name, l_name):
#     first = FIRST_NAME.get(f_name[0].upper())
#     last = SURNAME.get(l_name[0].upper())
#     return '{} {}'.format(first, last) if first and last else \
#         'Your name must start with a letter from A - Z.'
