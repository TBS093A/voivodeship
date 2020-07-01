
class Player:

    def __init__(self, name, clan=-1):
        self.playerName = name
        self.playerClan = clan
        self.gold = 250

class City(Player):
    
    def __init__(self, player):
        super().__init__(
            player.name, 
            player.clan, 
            player.gold
        )
        self.respect = 100


class Economy(City):

    def __init__(self, city):
        super().__init__(
            city.respect
        )
        self.people = 20
        self.materials = { "wood": 20, "stone": 20, "iron" = 20 }
        self.foodProcessed = { "flour": 0, "hop": 0 }
        self.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        self.weapon = { "spear": 0, "arch": 0, "crossbow": 0, "sword": 0, "plate_armor": 0 }
        self.entertainment = { "beer": 20 }

        self.buildings = {
            "general": { 
                "keep": 1, 
                "warehouse": 0, 
                "granary": 0, 
                "armory": 0 
            },
            "mine_raw_materials": { 
                "sawmill": 0,
                "stone_mine": 0,   
                "iron_mine": 0
            },
            "agriculture": { 
                "apple_orchard": 0,
                "grain_farm": 0, 
                "hop_plantation": 0, 
                "cow_farm": 0
            },
            "food_processing": {
                "mill": 0,
                "barkery": 0,
                "brawery": 0,
                "inn": 0
            }
            "workshops": { 
                "archery": 0, 
                "spearman": 0, 
                "crossbow": 0, 
                "forge": 0, 
                "armorer": 0 
            },
            "military": { 
                "barraks": 0,
                "engineers_guild": 0
            },
            "defense": {
                "wood_defense": { 
                    "palisade": 0, 
                    "small_wood_tower": 0, 
                    "big_wood_tower": 0, 
                    "small_wood_gate": 0,
                    "big_wood_gate": 0
                }
                "stone_defense": {
                    "wall": 0,
                    "medium_stone_tower": 0,
                    "big_stone_tower": 0,
                    "small_stone_gate": 0,
                    "big_stone_gate": 0
                }
                "other": {
                    "moat": 0,
                    "barricade": 0
                }
            }
        }

        # level of social

        self.taxesLevel = 0
        self.foodRationsLevel = 1
        self.peopleConsumptionLevel = 0

        # workers in city

        self.mineWorkers = 0
        self.agricultureWorkers = 0
        self.foodProcessingWorkers = 0
        self.workshopWorkers = 0

    def taxes(self):
        self.gold += self.people * self.taxesLevel
        self.respect -= level

    def foodRations(self):
        eat = self.people * self.foodRationsLevel
        foodValueSum = 0
        for type, value in self.food:
            if value > 0 and value >= eat:
                value -= eat
                self.respect += self.foodRationsLevel
                break
            else:
                foodValueSum += value
                if foodValueSum > 0 and foodValueSum > eat:
                    foodValueSum -= eat
                    self.respect += self.foodRationsLevel
                    value += foodValueSum
                    break
                else:
                    value = 0
        if foodValueSum == 0 or self.foodRationsLevel == 0:
            self.respect -= 16

    def peopleSatisfaction(self):
        consumption = self.people * self.peopleConsumptionLevel
        inns = self.buildings["food_processing"]["inn"]
        for type, value in self.entertainment:
            if type == "beer":
                consumption *= inns 
            if value > 0 and value >= consumption:
                self.respect += value / consumption
                value -= consumption
            else:
                self.respect += value / consumption
                value = 0

    def generalProduction(self):
        for buildType, buildings in self.buildings
            if buildType == "mine_raw_materials":
                workers = self.mineWorkers
            elif buildType == "agriculture":
                workers = self.agricultureWorkers
            elif buildType == "food_processing":
                workers = self.foodProcessingWorkers
            elif buildType == "workshops":
                workers = self.workshopWorkers
            for build, count in buildings:

    def mineProduction(self):
        for build, buildCount in self.buildings["mine_raw_materials"]:
            for mineral, value in self.materials:
                value += (self.mineWorkers / buildCount) 

    def farmProduction(self):
        for build, buildCount in self.buildings["agriculture"]:
            

    def foodProduction(self):
        for build, buildCount in self.buildings["food_processing"]:

    def workProduction(self):
        for build, buildCount in self.buildings["workshops"]:



class Build:

    def __init__(self, player):
        self.name = "abstractBuild"
        self.player = player
        self.HP = 100
        self.texture

    def getInfo(self):
        return f"Build name: {self.name}, HP: {self.HP}, player: {self.player}"

    class Meta:
        abstract = True

class Wall(Build):

    def __init__(self, player):
        super().__init__(player)
        self.name = "Stone Wall"
        self.HP = 300
        self.texture = pygame.image.load('wall.png').convert_alpha()

class House(Build):

    def __init__(self, player):
        super().__init__(player, HP)
        self.name = "House"
        self.texture = pygame.image.load('house.png').convert_alpha()

    def createPeople()
