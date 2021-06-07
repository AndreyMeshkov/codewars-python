# Basic subclasses - Adam and Eve
#
# https://www.codewars.com/kata/547274e24481cfc469000416
#
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve). The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman. Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
#

class Human():
    def __init__(self):
        pass


class Man(Human):
    def __init__(self):
        pass


class Woman(Human):
    def __init__(self):
        pass


def God():
    adam = Man()
    eve = Woman()
    return [adam, eve]

# Best practice:
#
#
# def God():
#     return [Man(), Woman()]
#
#
# class Human(object):
#     pass
#
#
# class Man(Human):
#     pass
#
#
# class Woman(Human):
#     pass

# Clever solution:
#
# Man, Woman, Human, God = (lambda h: ((lambda m, w, h: (m, w, h, lambda: (m(), w())))(type('Man', (h,), {}), type('Woman', (h,), {}), h)))(type('Human', (object,), {}))