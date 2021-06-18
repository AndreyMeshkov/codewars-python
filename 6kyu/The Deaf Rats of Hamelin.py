# The Deaf Rats of Hamelin
#
# https://www.codewars.com/kata/598106cb34e205e074000031
#
# Story
# The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.
#
# But some of the rats are deaf and are going the wrong way!
#
# Kata Task
# How many deaf rats are there?
#
# Legend
# P = The Pied Piper
# O~ = Rat going left
# ~O = Rat going right
# Example
# ex1 ~O~O~O~O P has 0 deaf rats
# ex2 P O~ O~ ~O O~ has 1 deaf rat
# ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

def count_deaf_rats(town):
    town = town.replace(' ', '')
    ind = town.index('P')
    left_part = town[0:ind]
    right_part = town[ind + 1:]
    result = [left_part[i:i + 2] for i in range(0, len(left_part), 2)].count(
        'O~')
    result += [right_part[i:i + 2] for i in range(0, len(right_part), 2)].count(
        '~O')
    return result

# Best practice and clever solution:
#
# def count_deaf_rats(town):
#     return town.replace(' ', '')[::2].count('O')
