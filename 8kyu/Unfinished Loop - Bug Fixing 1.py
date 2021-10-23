# Unfinished Loop - Bug Fixing #1
#
# https://www.codewars.com/kata/55c28f7304e3eaebef0000da
#
# Unfinished Loop - Bug Fixing #1
# Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished for loop!

def create_array(n):
    res = []
    i = 1
    while i <= n:
        res.append(i)
        i += 1
    return res

# Best practice:
#
# def create_array(n):
#     res=[]
#     i=1
#     while i<=n:
#         res+=[i]
#         i+= 1
#     return res

# Clever solution:
#
# def create_array(n):
#     return [i for i in range(1,n+1)]
