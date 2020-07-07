from player import *

class Country(Player):

    def __init__(self, name, player):
        self.player = player
        self.countryName = name
    
class Province(Country):

    def __init__(self, name, country):
        self.country = country
        self.provinceName = name
        self.respect = 100



