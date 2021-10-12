# Blackjack Scorer
#
# https://www.codewars.com/kata/534ffb35edb1241eda0015fe
#
# Complete the function that determines the score of a hand in the card game Blackjack (aka 21).
#
# The function receives an array of strings that represent each card in the hand ("2", "3", ..., "10", "J", "Q", "K" or "A") and should return the score of the hand (integer).
#
# Scoring rules:
# Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.
#
# Return the highest score of the cards that is less than or equal to 21. If there is no score less than or equal to 21 return the smallest score more than 21.
#
# Examples
# ["A"]                           ==>  11
# ["A", "J"]                      ==>  21
# ["A", "10", "A"]                ==>  12
# ["5", "3", "7"]                 ==>  15
# ["5", "4", "3", "2", "A", "K"]  ==>  25

def score_hand(cards):
    ten = ["J", "Q", "K"]
    aces = 0
    score = 0
    for card in cards:
        if card == "A":
            aces += 1
        elif card in ten:
            score += 10
        else:
            score += int(card)
    if score > 11 and aces > 0:
        score += aces
    elif score <= 10 and aces > 0:
        score += aces - 1
        if score > 10:
            score += 1
        else:
            score += 11
    return score

# Best practice and clever solution:
#
# def score_hand(a):
#     n = sum(11 if x == "A" else 10 if x in "JQK" else int(x) for x in a)
#     for _ in range(a.count("A")):
#         if n > 21:
#             n -= 10
#     return n
