
class Equipment:
    """
    A piece of equipment
    """
    def __init__(self, name, price):
        """
        creates the equipment, with name and price

        :param name: The name of the equipment
        :param price: its value in gp
        """
        self.name = name
        self.price = price

    def price_in_copper(self):
        """
        return the price in copper pieces

        :return: the value in cp
        """
        return self.price * 100

    def price_in_silver(self):
        """
        return the price in silver pieces

        :return: the value in sp
        """
        return self.price * 10

    def price_in_platinum(self):
        """
        return the price in platinum pieces

        :return: the value in pp
        """
        return self.price * 0.1


class Weapon(Equipment):
    """
    A weapon
    """
    def __init__(self, name, price, reach, dice, variant):
        """
        Create a weapon

        :param name: the weapons name
        :param price: its price in gp
        :param reach: its maximum reach
        :param dice: a Dice instance which calculates its damage
        :param variant: what the type of the weapon is
        """
        Equipment.__init__(self, name, price)
        self.reach = reach
        self.variant = variant
        self.dice = dice

    def calculate_damage(self):
        """
        Calculate the damage from the weapon, reset after

        :return: the value of the damage
        """
        temp = self.dice
        output = self.dice.calculate()
        self.dice = temp
        return output


class Armor(Equipment):
    """
    A piece of armor (or shield)
    """
    def __init__(self, name, price, ac):
        """
        Create a piece of armor

        :param name: The name of the armor
        :param price: its price
        :param ac: its bonus to AC
        """
        Equipment.__init__(self, name, price)
        self.ac = ac
