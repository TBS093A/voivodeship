# unique values

BUILD_TYPES = [
    # general
    "keep", "market", "warehouse", "granary", "armory", 
    # mine raw materials
    "sawmill", "stone_mine", "iron_mine",
    # agriculture
    "apple_orchard", "fisherman", "cow_farm", "grain_farm", "hop_plantation",
    # food processing
    "mill", "barkery", "brawery", "inn",
    # workshops
    "archery", "spearman", "crossbow", "forge", "armorer", 
    # society
    "small_houses", "medium_houses", "big_houses",
    # christian society
    "church", "cathedral", "basilica",
    # slavic society
    "mound", "peace_mound","war_mound",
    # military
    "barraks", "engineers_guild",
    # wood defense
    "palisade", "small_wood_tower", "big_wood_tower", "small_wood_gate", "big_wood_gate",
    # stone defense
    "wall", "medium_stone_tower", "big_stone_tower", "small_stone_gate", "big_stone_gate",
    # other defense
    "moat", "barricade"
]

class BuildType():

    def __init__(self, name, texture):
        self.name
        self.texture
    pass

    def draw(self, canvas, position):
        pass

class BuildFactory():

    buildTypes = [ BuildType(name, name + '.png') for name in BUILD_TYPES ]

    def __getitem__(self, name) -> BuildType:
        for buildType in self.buildTypes:
            if buildType.name == name:
                return buildType

# repeated values

class Build():

    def __init__(self, position, build_type):
        self.health_points = 100
        self.defend_points = 0
        self.position = position
        self.build_type = build_type 

    def rebuild(self):
        pass

    def upgrade(self):
        pass

    def draw(self, canvas):
        pass

# general functionality

class SettlementBuilder():

    buildings = []

    def __init__(self):     # default -> create one keep
        pass

    # builds methods

    def build(self, position, name) -> Build:
        buildType = BuildFactory[name]
        build = Build(position, buildType)
        self.buildings.append(build)
        return build

    def destroy(self, position) -> bool:
        pass


# class GeneralBuild(AbstractBuild):

#     general = { 
#                 "keep": 1,
#                 "market": 0, 
#                 "warehouse": 0, 
#                 "granary": 0, 
#                 "armory": 0 
#             }

# class MineRawMaterialsBuild(AbstractBuild):

#     mine_raw_materials = { 
#                 "sawmill": 0,
#                 "stone_mine": 0,   
#                 "iron_mine": 0
#             },

# class AgricultureBuild(AbstractBuild):

#     agriculture = { 
#                 "apple_orchard": 0,
#                 "fisherman": 0,
#                 "cow_farm": 0,
#                 "grain_farm": 0, 
#                 "hop_plantation": 0 
#             }

# class FoodProcessingBuild(AbstractBuild):

#     food_processing = {
#                 "mill": 0,
#                 "barkery": 0,
#                 "brawery": 0,
#                 "inn": 0
#             }
# class WorkshopBuild(AbstractBuild):

#     workshops = { 
#                 "archery": 0, 
#                 "spearman": 0, 
#                 "crossbow": 0, 
#                 "forge": 0, 
#                 "armorer": 0 
#             }

# class SocietyBuild(AbstractBuild):

#     society = {
#                 "small_houses": 0,
#                 "medium_houses": 0,
#                 "big_houses": 0,
#                 # christian
#                 "church": 0,        # on small settlement
#                 "cathedral": 0,     # on cities
#                 "basilica": 0,      # on province (city + settlements)
#                 # slavic
#                 "mound": 0,         # on small settlement
#                 "peace_mound": 0,   # on cities
#                 "war_mound": 0      # on province (city + settlements)
#             }

# class MilitaryBuild(AbstractBuild):

#     military = { 
#                 "barraks": 0,
#                 "engineers_guild": 0,
#                 "defense": {
#                     "wood_defense": { 
#                         "palisade": 0, 
#                         "small_wood_tower": 0, 
#                         "big_wood_tower": 0, 
#                         "small_wood_gate": 0,
#                         "big_wood_gate": 0
#                     },
#                     "stone_defense": {
#                         "wall": 0,
#                         "medium_stone_tower": 0,
#                         "big_stone_tower": 0,
#                         "small_stone_gate": 0,
#                         "big_stone_gate": 0
#                     },
#                     "other": {
#                         "moat": 0,
#                         "barricade": 0
#                     }
#                 }
#             }