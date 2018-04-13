# Microlite D20 monster generator
# Please note that I did not write the original version of this, and that I am only converting some JS that I found on 1d4chan.org
# I barely understand the retarded JS code, so I decided to convert it into something usable and readable that works

import random
import math
import re

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
# Feel free to expand the list of attack types
atktypes = 'Bite Claw Slam Gore Sting Tentacle Shock'
atktypes = atktypes + ' Broadsword Battleaxe Club Glaive Spear Falchion Dagger'

def randint(n):
    # Wierd way of doing random numbers, someone should probably rewrite this whole script to use the actual python random stuff
    return math.floor(random.randint(0, 1) * n)

def randItem(m):
    # grabs a random choice from the charectar dictionary np above
    return random.choice(np[m].split(' '))

def newword():
    # Generates a random name with some clever regex golf
    word = 'W'
    p = re.compile('[A-Z]')
    while len(word) < 40:
        match = re.search(p, word)
        if match:
            matched = match.group(0)
        else:
            return word.capitalize()
        word = word.replace(matched, randItem(matched))
    return word.capitalize()

def microMonster():
    # Generates stats and formats output
    hd = int(input("Enter number of hit dice(whole number): "))
    hd = hd * 1
    construct = "Name:" + newword() + "\n" + "HD: " + str(hd) + " (" + str(math.floor(hd * 4.5) + randint(hd * 4)) + "hp) "
    construct += ", AC: " + str((randint(5) + hd + 10)) + ", Attack: " + random.choice(atktypes.split(' ')) + " + " + str((hd + randint(4)))
    construct += " (" + str((randint(2) + 1)) + "d" + str((2 * ((randint(6) + 1)))) + ")\n"
    print(construct)
    return construct

microMonster()
