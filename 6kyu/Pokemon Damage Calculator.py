# Pokemon Damage Calculator
#
# https://www.codewars.com/kata/536e9a7973130a06eb000e9f
#
# It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):
#
# damage = 50 * (attack / defense) * effectiveness
# Where:
#
# attack = your attack power
# defense = the opponent's defense
# effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
# Effectiveness:
#
# Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.
#
# Super effective: 2x damage
# Neutral: 1x damage
# Not very effective: 0.5x damage
# To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:
#
# fire > grass
# fire < water
# fire = electric
# water < grass
# water < electric
# grass = electric
# For this kata, any type against itself is not very effective. Also, assume that the relationships between different types are symmetric (if A is super effective against B, then B is not very effective against A).
#
# The function you must implement takes in:
#
# your type
# the opponent's type
# your attack power
# the opponent's defense

matrix = [[0.5, 2.0, 0.5, 1.0],
          [0.5, 0.5, 2.0, 1.0],
          [2.0, 0.5, 0.5, 0.5],
          [1.0, 1.0, 2.0, 0.5]]
index = {"fire": 0, "grass": 1, "water": 2, "electric": 3}

def calculate_damage(your_type, opponent_type, attack, defense):
    return matrix[index[your_type]][index[opponent_type]] * 50 * attack / defense

# Best practice:
#
# import math
#
# effectiveness = {
#     "electric":{
#       "electric": 0.5,
#       "fire": 1,
#       "grass": 1,
#       "water": 2
#     },
#     "fire":{
#       "electric": 1,
#       "fire": 0.5,
#       "grass": 2,
#       "water": 0.5
#     },
#     "grass":{
#         "electric": 1,
#         "fire": 0.5,
#         "grass": 0.5,
#         "water": 2
#     },
#     "water":{
#         "electric": 0.5,
#         "fire": 2,
#         "grass": 0.5,
#         "water": 0.5
#     }
# }
#
# def calculate_damage(your_type, opponent_type, attack, defense):
#     return math.ceil(50 * (attack / defense) * effectiveness[your_type][opponent_type]);

# Clever solution:
#
# from math import ceil
#
# D = {"fire": "grass", "water": "fire", "grass": "water", "electric": "water"}
#
# def calculate_damage(a, b, n, m):
#     return ceil(50 * (n / m) * (2 if D[a] == b else 0.5 if D[b] == a or a == b else 1))
