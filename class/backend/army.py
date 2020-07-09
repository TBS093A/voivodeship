from .country import *

class Army():

    def __init__(self, country):
        self.country = country
        self.voivodes = []


class Voivode():

    def __init__(self, name, army, province):
        self.name = name
        
        self.army = army
        self.province = province

        self.morale = 100
        self.level = 1
        self.experience = 0
        
        self.economy_skills = {}
        self.warfare_skills = {}
        self.units = []

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