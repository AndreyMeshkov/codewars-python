# Grasshopper - Terminal Game Turn Function
#
# https://www.codewars.com/kata/56019d3b2c39ccde76000086
#
# Terminal game turn function
# You are creating a text-based terminal version of your favorite board game. In the board game, each turn has six steps that must happen in this order: roll the dice, move, combat, get coins, buy more health, and print status.
#
# You are using a library (Game.Logic in C#) that already has the functions below. Create a function named doTurn/DoTurn/do_turn that calls the functions in the proper order as described in the paragraph above.
#
# - `combat`
# - `buy_health`
# - `get_coins`
# - `print_status`
# - `roll_dice`

def do_turn():
    roll_dice()
    move()
    combat()
    get_coins()
    buy_health()
    print_status()

# Best practice:
#
# def do_turn():
#     roll_dice()
#     move()
#     combat()
#     get_coins()
#     buy_health()
#     print_status()
#
# Clever solution:
#
#
# def do_turn():
#     steps = [roll_dice, move, combat,
#              get_coins, buy_health, print_status]
#
#     for step in steps:
#         step()