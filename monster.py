# Microlite D20 monster generator
# Please note that I did not write the original version, and that I am only converting JS that I found on 1d4chan.org
# I barely understand the JS code, so I decided to convert it into something usable and readable that works

import random
import math
import re


class Monster:

    def __init__(self, hd, name=None, atktype=None, atk_bonus=None, hp=None, ac=None, sides=None, count=None):
        """
        Create monster from input, so existing monsters can be made into classes

        :param name: name of monster
        :param atktype: attack type
        :param atk_bonus: attack bonus
        :param hd: hit dice
        :param hp: hit points
        :param ac: Armor Class
        :param sides: atk dice number of sides
        :param count: number of attack dice
        :return: generated monster class
        """
        self.hd = hd
        if name is None:
            self.generate_monster()
        else:
            self.name = name
            self.atktype = atktype
            self.atk_bonus = atk_bonus
            self.hp = hp
            self.ac = ac
            self.sides = sides
            self.count = count

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

    def generate_monster(self):
        """
        Generates stats and formats output, assuming hit dice is a d8

        :return: sets class to random values
        """
        atktypes = 'Bite Claw Slam Gore Sting Tentacle Shock Broadsword Battleaxe Club Glaive Spear Falchion Dagger'

        # No dice class for simplicity
        def f(n): return random.randint(0, n)

        self.name = self.new_word()
        self.hp = int(math.floor(self.hd) * 4.5) + f(self.hd * 4)
        self.ac = f(5) + self.hd + 10
        self.atktype, self.atk_bonus = random.choice(atktypes.split(' ')), self.hd + f(4)
        self.count, self.sides = f(2) + 1, 2 * (f(6) + 1)
