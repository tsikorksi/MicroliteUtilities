# this may or may not be deleted


class Equipment:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type


class Weapon(Equipment):
    def __init__(self, name, value, reach, damage_count, damage_sides, type):
        Equipment.__init__(self, name, value, type)
        self.reach  = reach
        self.damage_count = damage_count
        self.damage_sides = damage_sides
