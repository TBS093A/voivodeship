class Clan():

    def __init__(self, name):
        self.name = name
        self.players = []

class Player():

    def __init__(self, name, clan):
        self.playerName = name
        self.playerClan = clan
        self.countries = []
        self.gold = 250