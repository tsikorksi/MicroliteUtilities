# Basic class allowing methods for dice rolling, without having to repeat the random calls
from random import randint as random


class Dice:

    @staticmethod
    def roller(count, sides):
        """
        rolls d6's
        :param sides: how many sides the dice has (d20, d6 etc)
        :param count: number of d6's to roll
        :return: array containing the values rolled
        """
        rolls = []

        for i in range(0, count):
            rolls.append(random.randint(1, sides))

        return rolls
