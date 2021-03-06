# String Templates - Bug Fixing #5
#
# https://www.codewars.com/kata/55c90cad4b0fe31a7200001f
#
# Oh no! Timmy hasn't followed instructions very carefully and forgot how to use the new String Template feature, Help Timmy with his string template so it works as he expects!

def build_string(*args):
    return "I like {0}!".format(", ".join(args))

# Best practice:
#
# def build_string(*args):
#     return "I like {}!".format(", ".join(args))
#
# Clever solution:
#
# def build_string(*args):
#     return f"I like {', '.join(args)}!"
