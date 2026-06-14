import random


def dice_roller(dice, count):
    """
        Dice roller function.
        Takes dice and roll count and
        returns sum.
        Args:
            dice: <int> basically the "sides"
            of the dice. Get random number
            between 1 and the dice int.
            count: <int> this is how many times
            we "roll" the dice basically.
            Get the random number between 1 and
            dice number COUNT many times.

        Returns:
            Number: <int> sum of all the rolls.
    """

    return sum([random.randint(1, dice) for i in range(count)])
