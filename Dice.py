import random


class Dice:

    def __init__(self, count, sides, bonus=0):
        """
        Generates an instance of dice, rolling them

        :param sides: 2dx
        :param count: xd6
        :param bonus: 3d6 + x
        """
        self.count = count
        self.sides = sides
        self.bonus = bonus

        self.result = 0
        self.rolls = []

    def calculate(self):
        """
        Get results of dice roll

        :return: populates result and rolls
        """
        for i in range(0, self.count):
            self.rolls[i] = random.randint(1, self.sides)
        self.result = sum(self.rolls) + self.bonus
        return self.result

    def calculate_rolls(self):
        """
        get the rolls of the dice

        :return: list of results
        """
        self.calculate()
        return self.rolls

    def print(self):
        """
        Pretty prints

        :return: N/A
        """
        print(f"Rolling {self.count}d{self.sides} + {self.bonus}...")
        print("The dice have come up as ", end='')
        print(f" {*self.rolls,}")
        print(f"Your total is {self.result}")
