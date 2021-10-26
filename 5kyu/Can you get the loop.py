# Can you get the loop ?
#
# https://www.codewars.com/kata/52a89c2ea8ddc5547a000863
#
# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.
#
# For example in the following picture the tail's size is 3 and the loop size is 12:
#
#
# # Use the `next' attribute to get the following node
# node.next
# Note: do NOT mutate the nodes!
#
# Thanks to shadchnev, I broke all of the methods from the Hash class.
#
# Don't miss dmitry's article in the discussion after you pass the Kata !!

def loop_size(node):
    current = node
    i = 1
    setattr(current, "visited", True)
    setattr(current, "n", i)
    while not hasattr(current.next, "visited"):
        current = current.next
        setattr(current, "visited", True)
        i += 1
        setattr(current, "n", i)
    n = (i + 1) - current.next.n
    return n

# Best practice and clever solution:
#
# def loop_size(node):
#     turtle, rabbit = node.next, node.next.next
#
#     # Find a point in the loop.  Any point will do!
#     # Since the rabbit moves faster than the turtle
#     # and the kata guarantees a loop, the rabbit will
#     # eventually catch up with the turtle.
#     while turtle != rabbit:
#         turtle = turtle.next
#         rabbit = rabbit.next.next
#
#     # The turtle and rabbit are now on the same node,
#     # but we know that node is in a loop.  So now we
#     # keep the turtle motionless and move the rabbit
#     # until it finds the turtle again, counting the
#     # nodes the rabbit visits in the mean time.
#     count = 1
#     rabbit = rabbit.next
#     while turtle != rabbit:
#         count += 1
#         rabbit = rabbit.next

    # voila
    return count
