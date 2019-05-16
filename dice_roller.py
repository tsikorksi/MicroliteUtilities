# Basic class allowing methods for dice rolling, without having to repeat the random calls
import operator as op
import random
import re


class Dice:

    @staticmethod
    def clean_rolls(total, rolls, adds, spec):
        """
        Prints the dice rolls in a clean way
        :param rolls: list of dice results
        :param total: total of all dice + bonus
        :param spec: dice roll entered
        :param adds: added bonus on the roll
        :return: nothing, prints to console
        """
        print("Rolling {} + {}...".format(spec, adds))
        print("The dice have come up as ", end='')
        print('(%s)' % ', '.join(map(str, rolls)))
        print("Your total is ", total)

    @staticmethod
    def dice_roll(spec):
        """
        rolls the values in the spec token
        :param spec: the postfix token
        :return: the sum of the rolls and bonus, the individual rolls and the bonus
        """
        match = re.match(r"(\d*)d(\d+)(([+-])(\d+))?", spec)
        dices = int(match.group(1) or "1")
        faces = int(match.group(2))
        adds = [1, -1][match.group(4) == "-"] * int(match.group(5)) if match.group(3) else 0
        rolls = [random.randint(1, faces) for _ in range(dices)]
        # print(" ".join(map(str, rolls)))
        return sum(rolls) + adds, rolls, adds, spec

    @staticmethod
    def rpn(line):
        """
        Reverse Polish Notation calculator
        Rolls dice based on an postfix input. Forms accepted are:
        - 4d6 12 +
        - 3d6 4 -
        - 2d4 5 *
        - 12d4 4 /
        :param line: the mathematical input
        :return: the final value
        """
        operators = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}
        stack = []
        rolls = []
        adds = 0
        spec = ''
        for token in line.split():
            print(token)
            if "d" in token:
                total, roll, adds, spec = Dice.dice_roll(token)
                rolls.append(roll)
                stack.append(total)
            elif token in operators:
                b, a = stack.pop(-1), stack.pop(-1)
                stack.append(operators[token](a, b))
                print(stack)
            else:
                try:
                    stack.append(int(token))
                    adds += int(token)
                except ValueError:
                    pass
        return stack[-1], rolls, adds, spec

    @staticmethod
    def roll(line, clean=False):
        """
        wrapper function for use elsewhere in the program
        :param line: the line of dice roll to calculate in postfix
        :param clean: whether or not to display a clean output
        :return:the total, the individual dice rolls, the bonus
        """
        total, rolls, adds, spec = Dice.rpn(line)
        if clean:
            Dice.clean_rolls(total, rolls, adds, spec)
        return total, rolls, adds


# if __name__ == "__main__":
#
#     for lines in sys.stdin:
#         total, rolls, adds, spec = Dice.rpn(lines)
#         Dice.clean_rolls(total, rolls, adds, spec)
