# Basic class allowing methods for dice rolling, without having to repeat the random calls
import random


class Dice:

    @staticmethod
    def roller(count, sides, bonus):
        """
        rolls d6's
        :param sides: how many sides the dice has (d20, d6 etc)
        :param count: number of d6's to roll
        :param bonus: the added bonus to the total roll
        :return: array containing the values rolled, the total score, as well as all the inputs
        """
        rolls = []

        for i in range(0, count):
            rolls.append(random.randint(1, sides))
        output = sum(rolls) + bonus

        Dice.clean_rolls(rolls, output, count, sides, bonus)

        return rolls, output, count, sides, bonus

    @staticmethod
    def clean_rolls(rolls, output, count, sides, bonus):
        print("Rolling {}d{} + {}...".format(count, sides, bonus))
        print("The dice have come up as ", end='')
        print('(%s)' % ', '.join(map(str, rolls)))
        print("Your total is ", output)


if __name__ == "__main__":
    dice = Dice
    dice.roller(4, 20, 10)
