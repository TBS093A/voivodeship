from country import *

class Army():

    voivodes = []

    def __init__(self, country):
        self.country = country


class Voivode():
    
    units = []
    economy_skills = {}
    warfare_skills = {}
    morale = 100
    level = 1
    experience = 0

    def __init__(self, name, army):
        self.army = army
        self.name = name

    def append_unit(self, unit):        # append unit
        self.units.append(unit)

    def __getitem__(self, index):       # get unit
        return units[index]

    def get_warfare_exp(self):          # battle wins
        pass

    def get_economy_exp(self):          # economy goals
        pass

    def set_warfare_skill(self):        # new skills in warfare
        pass

    def set_economy_skill(self):        # new skills in economy
        pass

    def cure_of_units(self):            # cure units -> 'leczenie jednostek'
        pass

    def upgrade_units(self):            
        pass

class Unit():

    def __init__(self, voivode):
        self.voivode = voivode
        self.count_of_warriors = 100
        self.damage_points = 1
        self.defend_points = 30

    def move(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass
    
    class Meta:
        abstract = True