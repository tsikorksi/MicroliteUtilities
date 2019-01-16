# Basic class allowing methods for dice rolling, without having to repeat the random calls
import random
import re


class Dice:

    @staticmethod
    def roller(count, sides, bonus):
        """
        rolls d6's
        :param sides: how many sides the dice has (d20, d6 etc)
        :param count: number of d6's to roll
        :param bonus: the added bonus to the total roll
        :return: dict containing the values rolled, the total score, as well as all the inputs
        """
        rolls = []

        for i in range(0, count):
            rolls.append(random.randint(1, sides))
        output = sum(rolls) + bonus

        # Dice.clean_rolls(rolls, output, count, sides, bonus)
        return {'rolls': rolls, 'output': output, 'count': count, 'sides': sides, 'bonus': bonus}

    @staticmethod
    def clean_rolls(rolls, output, count, sides, bonus):
        """
        Prints the dice rolls in a clean way
        :param rolls: list of dice results
        :param output: total of all dice + bonus
        :param count: number of dice rolled
        :param sides: sides on each dice
        :param bonus: added bonus on the roll
        :return: nothing, prints to console
        """
        print("Rolling {}d{} + {}...".format(count, sides, bonus))
        print("The dice have come up as ", end='')
        print('(%s)' % ', '.join(map(str, rolls)))
        print("Your total is ", output)

    @staticmethod
    def is_dice(dice_value):
        structure = re.compile("([1-9]\\d*)?d([1-9]\\d*)([/x][1-9]\\d*)?([+-]\\d+)?")
        if re.match(structure, dice_value) is not None:
            return True
        else:
            return False

    @staticmethod
    def calculate(equation_input):
        stack = []
        result = 0
        equation = equation_input.split(" ")
        for i in equation:
            if Dice.is_dice(i):
                stack.insert(0, i)
            else:

                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = ''
                    # TODO:calculate result of dice roll
                    stack.insert(0, str(result))
        return result


if __name__ == "__main__":
    dice = Dice
    dice.roller(4, 6, 0)
