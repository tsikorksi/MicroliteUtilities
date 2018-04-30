import json
import random


class Character:
    def __init__(self):
        self.name = str
        self.char_class = int
        self.race = int
        self.MIND = int
        self.STR = int
        self.DEX = int
        self.HP = int
        self.AC = int
        self.melee = int
        self.ranged = int
        self.magic = int
        self.physical = int
        self.subterfuge = int
        self.knowledge = int
        self.communication = int

    def char_gen(self):
        print("Generating character based on Microlite20 Revised Rules.")
        self.name = str(input("What is your characters name?"))
        response = True
        while response:
            print("Classes: \n \u2022"
                  " Fighters, "
                  "may wear any kind of armor and use shields, +3 bonus to Physical, +1 to all attack and damage rolls"
                  "\n \u2022 "
                  "Rogues, "
                  "may use light armor, +3 bonus to Subterfuge, after successful sneak may add Subterfuge to damage"
                  "\n \u2022 "
                  "Magi, "
                  "may not wear armor, +3 bonus to Knowledge, may cast Magi spells "
                  "\n \u2022"
                  " Clerics, "
                  "may use light or medium armor, +3 bonus to Communication,"
                  " can turn undead with Magic Attacks and cast Divine spells")
            class_response = str(input("Are they a Fighter[A], Rogue[B], Magi[C] or Cleric[D]?"))
            response = False
            if class_response == "A" or class_response == 'a':
                self.char_class = 0
            elif class_response == "B" or class_response == "b":
                self.char_class = 1
            elif class_response == "C" or class_response == "c":
                self.char_class = 2
            elif class_response == "D" or class_response == "d":
                self.char_class = 3
            else:
                response = True
        response = True
        while response:
            print("Races: \n \u2022 Humans, +1  to  all  skill  rolls\n \u2022 Elves, +2 MIND"
                  "\n \u2022 Dwarves, +2 STR \n \u2022 Halflings, +2 DEX")
            race_response = str(input("Are they a Human[A], Elf[B], Dwarf[C] or Halfling[D]?"))
            response = False
            if race_response == "A" or race_response == 'a':
                self.race = 0
            elif race_response == "B" or race_response == "b":
                self.race = 1
            elif race_response == "C" or race_response == "c":
                self.race = 2
            elif race_response == "D" or race_response == "d":
                self.race = 3
            else:
                response = True

        print("Attributes  represent  the  overall  physical  and  mental  qualities  of  an  individual."
              " They  define  the  raw  potential  an  individual  has  regardless  of  actual  skill.")
        print("To define these Attributes, the computer will roll 4D6, dropping the lowest roll, and you"
              " will choose which score to assign to 3 Attributes:\n \u2022 Strength(STR)"
              "\n \u2022 Dexterity(DEX)\n \u2022 Mind(MIND)")
        rolls = [0, 0, 0, 0]
        outs = [random.randint(1, 6) for _ in rolls]
        outs.remove(min(outs))
        print("Your rolls are {}.".format(outs))
        self.STR = int(input("Assign STR {}, {} or {}".format(outs[0], outs[1], outs[2])))
        outs.remove(self.STR)
        self.DEX = int(input("Assign DEX {} or {}".format(outs[0], outs[1])))
        outs.remove(self.DEX)
        self.MIND = outs[0]
        if self.race == 1:
            self.MIND += 2
        if self.race == 2:
            self.STR += 2
        if self.race == 3:
            self.DEX += 2

        self.HP = self.STR + 6
        self.AC = self.DEX + 10
        self.melee = self.STR + 1
        self.ranged = self.DEX + 1
        self.magic = self.MIND + 1

        self.physical = 1
        if self.char_class == 0:
            self.physical += 3
        self.subterfuge = 1
        if self.char_class == 1:
            self.subterfuge += 3
        self.knowledge = 1
        if self.char_class == 2:
            self.knowledge += 3
        self.communication = 1
        if self.char_class == 3:
            self.communication += 3

    def json_output(self):
        output = json.dumps(self.__dict__)
        print(output)
        return output


if __name__ == "__main__":
    zed = Character()
    Character.char_gen(zed)
    Character.json_output(zed)
