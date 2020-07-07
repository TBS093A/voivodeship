class BuildFactory():

    buildings = []

    def __init__(self):     # default -> create one keep
        pass

    # builds methods

class AbstractBuild():

    def __init__(self):
        self.health_points = 100
        self.defend_points = 0

    def rebuild(self):
        pass

    def upgrade(self):
        pass

    class Meta:
        abstract = True
    
class GeneralBuild(AbstractBuild):

    general = { 
                "keep": 1,
                "market": 0, 
                "warehouse": 0, 
                "granary": 0, 
                "armory": 0 
            }

class MineRawMaterialsBuild(AbstractBuild):

    mine_raw_materials = { 
                "sawmill": 0,
                "stone_mine": 0,   
                "iron_mine": 0
            },

class AgricultureBuild(AbstractBuild):

    agriculture = { 
                "apple_orchard": 0,
                "fisherman": 0,
                "cow_farm": 0,
                "grain_farm": 0, 
                "hop_plantation": 0 
            }

class FoodProcessingBuild(AbstractBuild):

    food_processing = {
                "mill": 0,
                "barkery": 0,
                "brawery": 0,
                "inn": 0
            }
class WorkshopBuild(AbstractBuild):

    workshops = { 
                "archery": 0, 
                "spearman": 0, 
                "crossbow": 0, 
                "forge": 0, 
                "armorer": 0 
            }

class SocietyBuild(AbstractBuild):

    society = {
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
            }

class MilitaryBuild(AbstractBuild):

    military = { 
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