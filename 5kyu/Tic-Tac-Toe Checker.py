# Tic-Tac-Toe Checker
#
# https://www.codewars.com/kata/525caa5c1bf619d28c000335
#
# If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!
#
# Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:
#
# [[0, 0, 1],
#  [0, 1, 2],
#  [2, 1, 0]]
# We want our function to return:
#
# -1 if the board is not yet finished AND no one has won yet (there are empty spots),
# 1 if "X" won,
# 2 if "O" won,
# 0 if it's a cat's game (i.e. a draw).
# You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.

def is_solved(board):
    if is_winner(1, board):
        return 1
    if is_winner(2, board):
        return 2
    count_zero = 0
    for row in board:
        if 0 in row:
            count_zero += 1
    if count_zero == 0:
        return 0
    return -1


def is_winner(num, board):
    for row in board:
        if row.count(num) == 3:
            return True
    count_col0 = 0
    count_col1 = 0
    count_col2 = 0
    count_diag1 = 0
    count_diag2 = 0
    for i in range(0, 3):
        if board[i][0] == num:
            count_col0 += 1
        if board[i][1] == num:
            count_col1 += 1
        if board[i][2] == num:
            count_col2 += 1
        if board[i][i] == num:
            count_diag1 += 1
        if board[2 - i][i] == num:
            count_diag2 += 1
    if count_col0 == 3 or count_diag1 == 3 or count_diag2 == 3 or count_col1 == 3 or count_col2 == 3:
        return True

# Best practice:
#
#
# def isSolved(board):
#     for i in range(0, 3):
#         if board[i][0] == board[i][1] == board[i][2] != 0:
#             return board[i][0]
#         elif board[0][i] == board[1][i] == board[2][i] != 0:
#             return board[0][i]
#
#     if board[0][0] == board[1][1] == board[2][2] != 0:
#         return board[0][0]
#     elif board[0][2] == board[1][1] == board[2][0] != 0:
#         return board[0][0]
#
#     elif 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
#         return 0
#     else:
#         return -1
#
# Clever solution:
#
# import itertools
#
# def isSolved(board):
#     b = list(itertools.chain(*board))
#     for p, q, r in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
#         if b[p] == b[q] == b[r] != 0: return b[p]
#     return 0 if sum(b) == 13 else -1
