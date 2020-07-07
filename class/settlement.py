from country import *

class City(Province):
    
    def __init__(self, name, province):
        self.province = province
        self.cityName = name

        self.people = 20
        self.materials = { "wood": 20, "stone": 20, "iron": 20 }
        self.foodProcessed = { "grain": 0, "flour": 0, "hop": 0 }
        self.food = { "apple": 20, "fish": 20, "chees": 20, "bread": 20 }
        self.foodEatingBlock = { "apple": False, "fish": False, "chees": False, "bread": False }
        self.weapon = { "spear": 0, "arch": 0, "crossbow": 0, "sword": 0, "plate_armor": 0 }
        self.entertainment = { "beer": 20 }

        self.buildings = {
            "general": { 
                "keep": 1,
                "market": 0, 
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
                "fisherman": 0,
                "cow_farm": 0,
                "grain_farm": 0, 
                "hop_plantation": 0 
            },
            "food_processing": {
                "mill": 0,
                "barkery": 0,
                "brawery": 0,
                "inn": 0
            },
            "workshops": { 
                "archery": 0, 
                "spearman": 0, 
                "crossbow": 0, 
                "forge": 0, 
                "armorer": 0 
            },
            "people": {
                "small_houses": 0,
                "medium_houses": 0,
                "big_houses": 0,
                # christian
                "church": 0,        # on small settlement
                "cathedral": 0,     # on cities
                "basilica": 0,      # on province (city + settlements)
                # slavic
                "mound": 0,         # on small settlement
                "peace_mound": 0,   # on cities
                "war_mound": 0      # on province (city + settlements)
            },
            "military": { 
                "barraks": 0,
                "engineers_guild": 0,
                "defense": {
                    "wood_defense": { 
                        "palisade": 0, 
                        "small_wood_tower": 0, 
                        "big_wood_tower": 0, 
                        "small_wood_gate": 0,
                        "big_wood_gate": 0
                    },
                    "stone_defense": {
                        "wall": 0,
                        "medium_stone_tower": 0,
                        "big_stone_tower": 0,
                        "small_stone_gate": 0,
                        "big_stone_gate": 0
                    },
                    "other": {
                        "moat": 0,
                        "barricade": 0
                    }
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

    def collectTaxes(self):
        self.province.country.player.gold += self.people * self.taxesLevel
        self.province.respect -= self.taxesLevel

    def foodRations(self):
        hungryPeople = self.people * self.foodRationsLevel
        if self.foodRationsLevel == 0:
            self.province.respect -= 16
        else:
            for foodType, foodValue in self.food.items():
                if self.foodEatingBlock[foodType] == False:
                    hungryPeople -= self.food[foodType]
                    if hungryPeople <= 0:
                        self.food[foodType] = int( -hungryPeople )
                        if self.province.respect + self.foodRationsLevel > 100:
                            self.province.respect = 100
                        else:
                            self.province.respect += self.foodRationsLevel * 4      # all be fine
                        break
                    if hungryPeople > 0:
                        self.food[foodType] = 0

            if hungryPeople > 0:
                self.province.respect -= 16                                         # with food something wrong
            elif self.foodRationsLevel > 0 and self.foodRationsLevel < 1:
                self.province.respect -= int(16 * ( 1 - self.foodRationsLevel ))
                

    def peopleSatisfaction(self):
        consumption = self.people * self.peopleConsumptionLevel
        inns = self.buildings["food_processing"]["inn"]
        if consumption != 0 and inns != 0:
            for EntType, EntValue in self.entertainment.items():
                if EntType == "beer":
                    consumption *= inns 
                if EntValue > 0 and EntValue >= consumption:
                    self.province.respect += (EntValue / consumption) * 5
                    if self.province.respect > 100:
                        self.province.respect = 100
                    self.entertainment[EntType] -= consumption
                else:
                    self.province.respect += (EntValue / consumption) * 5
                    if self.province.respect > 100:
                        self.province.respect = 100
                    self.entertainment[EntType] = 0

    # def generalProduction(self):
    #     for buildType, buildings in self.buildings:
    #         if buildType == "mine_raw_materials":
    #             workers = self.mineWorkers
    #         elif buildType == "agriculture":
    #             workers = self.agricultureWorkers
    #         elif buildType == "food_processing":
    #             workers = self.foodProcessingWorkers
    #         elif buildType == "workshops":
    #             workers = self.workshopWorkers
    #         for build, count in buildings:

    def mineProduction(self):
        for build, buildCount in self.buildings["mine_raw_materials"]:
            for mineral, value in self.materials:
                value += (self.mineWorkers / buildCount) 

    # def farmProduction(self):
    #     for build, buildCount in self.buildings["agriculture"]:
            

    # def foodProduction(self):
    #     for build, buildCount in self.buildings["food_processing"]:

    # def workProduction(self):
    #     for build, buildCount in self.buildings["workshops"]: