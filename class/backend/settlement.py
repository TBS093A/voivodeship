from .country import *
from .build import *

class City():
    
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

        # builder

        self.buildings = SettlementBuilder()

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
                
    # TODO upgrade people satisfaction
    # 1 inn per 50 people need 10 beer's for +20 respect
    #                     need 5  beer's for +15 respect
    #                     need 3  beer's for +10 respect
    #                     need 2  beer's for +5  respect
    #                     need 1  beer   for +2  respect 
    
    def peopleSatisfaction(self):
        consumption = self.people * self.peopleConsumptionLevel
        inns = self.buildings.count_builds_by_name('inn')
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

class Village():

    def __init__(self, name, city):
        self.city = city
        self.name = name