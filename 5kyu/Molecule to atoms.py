# Molecule to atoms
#
# https://www.codewars.com/kata/52f831fa9d332c6591000511
#
# For a given chemical formula represented by a string, count the number of atoms of each element contained in the molecule and return an object (associative array in PHP, Dictionary<string, int> in C#, Map<String,Integer> in Java).
#
# For example:
#
# water = 'H2O'
# parse_molecule(water)                 # return {H: 2, O: 1}
#
# magnesium_hydroxide = 'Mg(OH)2'
# parse_molecule(magnesium_hydroxide)   # return {Mg: 1, O: 2, H: 2}
#
# var fremy_salt = 'K4[ON(SO3)2]2'
# parse_molecule(fremySalt)             # return {K: 4, O: 14, N: 2, S: 4}
# As you can see, some formulas have brackets in them. The index outside the brackets tells you that you have to multiply count of each atom inside the bracket on this index. For example, in Fe(NO3)2 you have one iron atom, two nitrogen atoms and six oxygen atoms.
#
# Note that brackets may be round, square or curly and can also be nested. Index after the braces is optional.

import re


def parse_molecule(formula):
    pattern = r'[A-Z][a-z]?'
    pattern2 = r'\d+'
    map_dict = {'(': ')', '{': '}', '[': ']'}
    i = 0
    temp_dict = {}
    while i < len(formula):
        ss = re.match(pattern, formula[i:])
        if ss is not None:
            if ss.group(0).isalpha():
                i += len(ss.group(0))
                ss2 = re.match(pattern2, formula[i:])
                if ss2 is not None:
                    if ss2.group(0).isdigit():
                        i += len(ss2.group(0))
                        temp_dict[ss.group(0)] = int(
                            ss2.group(0)) + temp_dict.get(ss.group(0), 0)
                    else:
                        temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0),
                                                                   0)
                else:
                    temp_dict[ss.group(0)] = 1 + temp_dict.get(ss.group(0), 0)
        elif formula[i] in map_dict:
            index = formula[i:].index(map_dict[formula[i]])
            temp_dict2 = parse_molecule(formula[i + 1:i + index])
            i += index + 1
            ss2 = re.match(pattern2, formula[i:])
            if ss2 is not None:
                if ss2.group(0).isdigit():
                    i += len(ss2.group(0))
                    for item in temp_dict2:
                        temp_dict2[item] *= int(ss2.group(0))
            for item in temp_dict2:
                temp_dict[item] = temp_dict2[item] + temp_dict.get(item, 0)
    return temp_dict

# Best practice and clever solution:
#
# from collections import Counter
# import re
#
# COMPONENT_RE = (
#     r'('
#         r'[A-Z][a-z]?'
#         r'|'
#         r'\([^(]+\)'
#         r'|'
#         r'\[[^[]+\]'
#         r'|'
#         r'\{[^}]+\}'
#     r')'
#     r'(\d*)'
# )
#
#
# def parse_molecule(formula):
#     counts = Counter()
#     for element, count in re.findall(COMPONENT_RE, formula):
#         count = int(count) if count else 1
#         if element[0] in '([{':
#             for k, v in parse_molecule(element[1:-1]).items():
#                 counts[k] += count * v
#         else:
#             counts[element] += count
#     return counts
