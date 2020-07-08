from functionality import Functionality

class World():

    def __init__(self):
        self.landscape_map = []
        self.clans_map = []
        self.countries_map = []
        self.provinces_map = []
        self.settlements_map = []

        self.functionality = Functionality()

    def generate_world(self, size):
        for next_array in range(size):
            array = []
            for tileType in range(size):
                array.append(0)
            self.landscape_map.append(array)
            
