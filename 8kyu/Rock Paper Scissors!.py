# Rock Paper Scissors!
#
# https://www.codewars.com/kata/5672a98bdbdd995fad00000f
#
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.
#
# Examples:
#
# rps('scissors','paper') // Player 1 won!
# rps('scissors','rock') // Player 2 won!
# rps('paper','paper') // Draw!

def rps(p1, p2):
    lst = ["paper", "scissors", "rock"]
    if p1 == p2:
        return "Draw!"
    if p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    if p2 == "rock" and p1 == "paper":
        return "Player 1 won!"
    if lst.index(p1) > lst.index(p2):
        return "Player 1 won!"
    if lst.index(p2) > lst.index(p1):
        return "Player 2 won!"

# Best practice:
#
# def rps(p1, p2):
#     beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
#     if beats[p1] == p2:
#         return "Player 1 won!"
#     if beats[p2] == p1:
#         return "Player 2 won!"
#     return "Draw!"

# Clever solution:
#
# def rps(p1, p2):
#     hand = {'rock':0, 'paper':1, 'scissors':2}
#     results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
#     return results[hand[p1] - hand[p2]]
