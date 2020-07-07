class Player:

    countries = []
    gold = 250

    def __init__(self, name, clan=-1):
        self.playerName = name
        self.playerClan = clan