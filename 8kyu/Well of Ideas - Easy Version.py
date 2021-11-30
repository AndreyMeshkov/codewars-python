# Well of Ideas - Easy Version
#
# https://www.codewars.com/kata/57f222ce69e09c3630000212
#
# For every good kata idea there seem to be quite a few bad ones!
#
# In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

def well(x):
    good_ideas = len([i for i in x if i == "good"])
    if good_ideas > 2:
        return "I smell a series!"
    elif good_ideas > 0:
        return "Publish!"
    else:
        return "Fail!"

# Best practice and clever solution:
#
# def well(x):
#     c = x.count('good')
#     return 'I smell a series!' if c > 2 else 'Publish!' if c else 'Fail!'
