# Switch/Case - Bug Fixing #6
#
# https://www.codewars.com/kata/55c933c115a8c426ac000082
#
# Switch/Case - Bug Fixing #6
# Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object, can you fix timmy's function?

def eval_object(v):
    return {"+": v['a'] + v['b'],
            "-": v['a'] - v['b'],
            "/": v['a'] / v['b'],
            "*": v['a'] * v['b'],
            "%": v['a'] % v['b'],
            "**": v['a'] ** v['b']
            }.get(v['operation'])

# Best practice:
#
# def eval_object(v):
#     return {"+": v['a']+v['b'],
#             "-": v['a']-v['b'],
#             "/": v['a']/v['b'],
#             "*": v['a']*v['b'],
#             "%": v['a']%v['b'],
#            "**": v['a']**v['b'], }.get(v['operation'])
#
# Clever solution:
#
# def eval_object(v):
#     return eval("{a}{operation}{b}".format(**v))
