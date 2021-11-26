# Alphabet war - airstrike - letters massacre
#
# https://www.codewars.com/kata/5938f5b606c3033f4700015a
#
# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spreaded everywhere on the battlefield.
#
# Task
# Write a function that accepts fight string consists of only small letters and * which means a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.
#
# The left side letters and their power:
#
#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:
#
#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims.
# The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );
#
# Example
# AlphabetWar("s*zz");           //=> Right side wins!
# AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
# AlphabetWar("zzzz*s*");       //=> Right side wins!
# AlphabetWar("www*www****z");  //=> Left side wins!
# Alphabet war Collection
# Alphavet war
# Alphabet war - airstrike - letters massacre
# Alphabet wars - reinforces massacre
# Alphabet wars - nuclear strike
# Alphabet war - Wo lo loooooo priests join the war

def alphabet_war(fight):
    letters = list(" " + fight + " ")
    for i in range(1, len(fight) + 1):
        if letters[i] == "*":
            letters[i - 1] = "-"
            if letters[i + 1] != "*":
                letters[i + 1] = "-"
    left_sum = 0
    right_sum = 0
    left_letters = ["s", "b", "p", "w"]
    right_letters = ["z", "d", "q", "m"]
    for i in letters:
        if i in left_letters:
            left_sum += left_letters.index(i) + 1
        if i in right_letters:
            right_sum += right_letters.index(i) + 1
    if left_sum == right_sum:
        return "Let's fight again!"
    elif left_sum > right_sum:
        return "Left side wins!"
    elif right_sum > left_sum:
        return "Right side wins!"

# Best practice:
#
# import re
#
# powers = {
#     'w': -4, 'p': -3, 'b': -2, 's': -1,
#     'm': +4, 'q': +3, 'd': +2, 'z': +1,
# }
#
# def alphabet_war(fight):
#     fight = re.sub('.(?=\*)|(?<=\*).', '', fight)
#     result = sum(powers.get(c, 0) for c in fight)
#     if result < 0:
#         return 'Left side wins!'
#     elif result > 0:
#         return 'Right side wins!'
#     else:
#         return "Let's fight again!"

# Clever solution:
#
# import re;alphabet_war=lambda s:["Let's fight again!","Left side wins!","Right side wins!"][
# cmp(sum(i*n for i,n in enumerate(map(re.sub('.?\*+.?','',s).count,'mqdz*sbpw'),-4)),0)]