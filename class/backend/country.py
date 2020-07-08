from .player import *

class Country():

    def __init__(self, name, player):
        self.player = player
        self.countryName = name
        self.provinces = []
    
class Province():

    def __init__(self, name, country):
        self.country = country
        self.provinceName = name
        self.respect = 100
        self.cities = []



