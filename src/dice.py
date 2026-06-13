import random


def dice_roller(dice, count):

    return sum([random.randint(1, dice) for i in range(count)])
