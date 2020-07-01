import random

class TileMap:

    def __init__(self, size):
        self._tileMap = self.createMap(size)
        self._tiles = []
        for row in self._tileMap:
            for x in row:
                self._tiles.append( { "status": x } )
    
    def loadingMap(self, oldMap):
        self._tileMap = oldMap
        self._tiles = []
        for row in self._tileMap:
            for x in row:
                self._tiles.append( { "status": x } )

    def appendTile(self, polygon, position):
        for tile in self._tiles:
            if "polygon" not in tile:
                tile["polygon"] = polygon
                tile["position"] = position
                break

    def __getitem__(self, index):
        return self._tileMap[index]

    def updateMap(self, index, status):
        newMap = self._tileMap
        size = len(newMap)
        rowIndex = int(index / size)
        realIndex = index - (rowIndex * size)
        self._tileMap[rowIndex][realIndex] = status

    def getTile(self, index):
        return self._tiles[index]

    @staticmethod
    def createMap(size) -> list:
        """
        Create `size` x `size` map
        """
        map_data = []
        for mapy in range(0, size):
            map_row = []
            for mapx in range(0, size):
                map_row.append(0) # random.randint(0,1)
            map_data.append(map_row)
        return map_data 