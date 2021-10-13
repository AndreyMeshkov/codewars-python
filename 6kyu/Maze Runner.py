# Maze Runner
#
# https://www.codewars.com/kata/58663693b359c4a6560001d6
#
# Introduction
# Welcome Adventurer. Your aim is to navigate the maze and reach the finish point without touching any walls. Doing so will kill you instantly!
# Task
# You will be given a 2D array of the maze and an array of directions. Your task is to follow the directions given. If you reach the end point before all your moves have gone, you should return Finish. If you hit any walls or go outside the maze border, you should return Dead. If you find yourself still in the maze after using all the moves, you should return Lost.
# The Maze array will look like
#
# maze = [[1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,3],
#         [1,0,1,0,1,0,1],
#         [0,0,1,0,0,0,1],
#         [1,0,1,0,1,0,1],
#         [1,0,0,0,0,0,1],
#         [1,2,1,0,1,0,1]]
# ..with the following key
#
#       0 = Safe place to walk
#       1 = Wall
#       2 = Start Point
#       3 = Finish Point
#   direction = ["N","N","N","N","N","E","E","E","E","E"] == "Finish"
# Rules
# 1. The Maze array will always be square i.e. N x N but its size and content will alter from test to test.
#
# 2. The position and finish positions will change for the final tests.
#
# 3. The directions array will always be in upper case and will be in the format of N = North, E = East, W = West and S = South.
#
# 4. If you reach the end point before all your moves have gone, you should return Finish.
#
# 5. If you hit any walls or go outside the maze border, you should return Dead.
#
# 6. If you find yourself still in the maze after using all the moves, you should return Lost.
# Good luck, and stay safe!

def maze_runner(maze, directions):
    position = []
    for i in maze:
        if 2 in i:
            position.append(i.index(2))
            position.append(maze.index(i))
    max_pos = len(maze) - 1
    for direction in directions:
        if direction == 'S':
            position[1] += 1
        elif direction == 'N':
            position[1] -= 1
        elif direction == 'E':
            position[0] += 1
        elif direction == 'W':
            position[0] -= 1
        if position[0] < 0 or position[0] > max_pos or position[1] < 0 or \
                position[1] > max_pos or maze[position[1]][position[0]] == 1:
            return 'Dead'
        elif maze[position[1]][position[0]] == 3:
            return 'Finish'
    return 'Lost'

# Best practice:
#
# def maze_runner(maze, directions):
#     n = len(maze)
#
#     # find start point
#     for i in range(n):
#         if 2 in maze[i]:
#             row = i
#             col = maze[row].index(2)
#             break
#
#     # follow directions
#     for step in directions:
#         if step == "N":
#             row -= 1
#         elif step == "S":
#             row += 1
#         elif step == "E":
#             col += 1
#         elif step == "W":
#             col -= 1
#
#         # check the result
#         if row < 0 or col < 0 or row == n or col == n or maze[row][col] == 1:
#             return "Dead"
#         elif maze[row][col] == 3:
#             return "Finish"
#
#     return "Lost"

# Clever solution:
#
# DIRS = {'S': (1,0), 'E': (0,1), 'N': (-1,0), 'W': (0,-1)}
#
# def maze_runner(maze, directions):
#     maze = [l + [1] for l in maze] + [[1] * len(maze[0])]
#     y, x = next((y,x) for y, l in enumerate(maze) for x, c in enumerate(l) if c == 2)
#     for dy, dx in map(DIRS.get, directions):
#         y += dy; x += dx
#         if maze[y][x] == 3: return 'Finish'
#         if maze[y][x] == 1: return 'Dead'
#     return 'Lost'
