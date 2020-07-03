# Microlite D20 monster generator
# Please note that I did not write the original version, and that I am only converting JS that I found on 1d4chan.org
# I barely understand the JS code, so I decided to convert it into something usable and readable that works

import random
import math
import re


class Monster:

    def __init__(self):
        self.name = str
        self.atktype = str
        self.atk_bonus = int
        self.hd = int
        self.hp = int
        self.ac = int
        self.atk_dice_sides = int
        self.atk_dice_count = int

    def create(self, name, atktype, atk_bonus, hd, hp, ac, atk_dice_sides, atk_dice_count):
        """
        Create monster from input, so existing monsters can be made into classes

        :param name: name of monster
        :param atktype: attack type
        :param atk_bonus: attack bonus
        :param hd: hit dice
        :param hp: hit points
        :param ac: Armor Class
        :param atk_dice_sides: atk dice number of sides
        :param atk_dice_count: number of attack dice
        :return:
        """
        self.name = name
        self.atktype = atktype
        self.atk_bonus = atk_bonus
        self.hd = hd
        self.hp = hp
        self.ac = ac
        self.atk_dice_sides = atk_dice_sides
        self.atk_dice_count = atk_dice_count

    @staticmethod
    def new_word():
        """
        Generates a random name with some clever regex golf, by replacing capital letters with selected letter combos
        :return: The new name
        """
        np = {
             'W': 'CT CT CX CDF CVFT CDFU CTU IT ICT A',
             'A': 'KVKVtion',
             'K': 'b c d f g j l m n p qu r s t v sP',
             'I': 'ex in un re de',
             'T': 'VF VEe',
             'U': 'er ish ly en ing ness ment able ive',
             'C': 'b c ch d f g h j k l m n p qu r s sh t th v w y sP Rr Ll',
             'E': 'b c ch d f g dg l m n p r s t th v z',
             'F': 'b tch d ff g gh ck ll m n n ng p r ss sh t tt th x y zz rR sP lL',
             'P': 'p t k c',
             'Q': 'b d g',
             'L': 'b f k p s',
             'R': 'P Q f th sh',
             'V': 'a e i o u',
             'D': 'aw ei ow ou ie ea ai oy',
             'X': 'e i o aw ow oy'
         }
        word = 'W'
        p = re.compile('[A-Z]')
        while len(word) < 40:
            match = re.search(p, word)
            if match:
                matched = match.group(0)
            else:
                return word.capitalize()
            word = word.replace(matched, random.choice(np[matched].split(' ')))
        return word.capitalize()

    def micro_monster(self):
        """
        Generates stats and formats output, assuming hit dice is a d8

        :return: sets class to random values
        """
        atktypes = 'Bite Claw Slam Gore Sting Tentacle Shock Broadsword Battleaxe Club Glaive Spear Falchion Dagger'

        def f(n): return random.randint(0, n)
        self.hd = int(input("Number of hit-dice?"))

        self.name = self.new_word()
        self.hp = int(math.floor(self.hd) * 4.5) + f(self.hd * 4)
        self.ac = f(5) + self.hd + 10
        self.atktype, self.atk_bonus = random.choice(atktypes.split(' ')), self.hd + f(4)
        self.atk_dice_count, self.atk_dice_sides = f(2) + 1, 2 * (f(6) + 1)


if __name__ == "__main__":
    monst = Monster()

    monst.micro_monster()

# hd = int(input("Enter number of hit dice(whole number): "))
# micro_monster(hd)
