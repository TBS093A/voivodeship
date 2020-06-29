import pygame
from pygame.locals import *
import sys
import random
import time

# tile map class

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
                map_row.append(random.randint(0,1))
            map_data.append(map_row)
        return map_data 

# menu functionality class

class GeneralMenu:

    def __init__(self, screen):
        self.screenX = pygame.display.Info().current_w
        self.screenY = pygame.display.Info().current_h  
        self._menu = pygame.draw.rect(screen, 255, ((0,self.screenY), (self.screenX, -100)))

# screen 

def scrollMap(screen, map_data, scroll):
    timeM = time.time()
    wall = pygame.image.load('wall.png').convert_alpha()
    grass = pygame.image.load('grass.png').convert_alpha()
    
    TILEWIDTH = 64  #holds the tile width and height
    TILEHEIGHT = 64
    TILEHEIGHT_HALF = TILEHEIGHT /2
    TILEWIDTH_HALF = TILEWIDTH /2
    
    screenX = pygame.display.Info().current_w
    screenY = pygame.display.Info().current_h  
    pygame.draw.rect(screen, 0, ((0,screenY), (screenX, -screenY)))  # mask

    for row_nb, row in enumerate(map_data):    #for every row of the map...
        for col_nb, tile in enumerate(row):
            if tile == 1:
                tileImage = wall
            else:
                tileImage = grass
            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF  
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y)/2
            
            centered_x = screen.get_rect().centerx + iso_x + scroll[0]
            centered_y = screen.get_rect().centery/2 + iso_y + scroll[1]

            top = (centered_x, centered_y + 16)
            left = (centered_x - 32, centered_y)
            bottom = (centered_x, centered_y - 16)
            right = (centered_x + 32, centered_y)
            position = { "top": top, "right": right, "bottom": bottom, "left": left}

            polygon = pygame.draw.polygon(screen, 0, (top, right, bottom, left))
            map_data.appendTile(polygon, position)
            screen.blit(tileImage, (centered_x - 32, centered_y - 47))
    pygame.display.update()
    print(f"scrollmap method: {time.time() - timeM}s")


def loadWorld(screen, map_data, map_size):
    """
    Create new world map
    """
    timeM = time.time()
    wall = pygame.image.load('wall.png').convert_alpha()
    grass = pygame.image.load('grass.png').convert_alpha()
    
    TILEWIDTH = 64  #holds the tile width and height
    TILEHEIGHT = 64
    TILEHEIGHT_HALF = TILEHEIGHT /2
    TILEWIDTH_HALF = TILEWIDTH /2
    
    for row_nb, row in enumerate(map_data):    #for every row of the map...
        for col_nb, tile in enumerate(row):
            if tile == 1:
                tileImage = wall
            else:
                tileImage = grass
            cart_x = row_nb * TILEWIDTH_HALF
            cart_y = col_nb * TILEHEIGHT_HALF  
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y)/2
            
            centered_x = screen.get_rect().centerx + iso_x
            centered_y = screen.get_rect().centery/2 + iso_y

            top = (centered_x, centered_y + 16)
            left = (centered_x - 32, centered_y)
            bottom = (centered_x, centered_y - 16)
            right = (centered_x + 32, centered_y)
            position = { "top": top, "right": right, "bottom": bottom, "left": left}

            polygon = pygame.draw.polygon(screen, 0, (top, right, bottom, left))
            map_data.appendTile(polygon, position)
            screen.blit(tileImage, (centered_x - 32, centered_y - 47))
    print(f"loadworld method: {time.time() - timeM}s")

def refreshWorld(screen, map_data, map_size):
    """
    Clear screen (hide open menus itp)
    """
    timeM = time.time()
    loadWorld(screen, map_data, map_size) # refresh world
    pygame.display.update()
    print(f"refreshworld method: {time.time() - timeM}s")

# events

def leftClickAction(screen, map_data, map_size, MOUSE_POSITION, action, activeMenu):
    timeM = time.time()
    for index, tile in enumerate(map_data._tiles):
        if tile["polygon"].collidepoint(MOUSE_POSITION):
            if action["active"]:    # build
                map_data.updateMap(index, 1)
                loadWorld(screen, map_data, map_size)
                pygame.display.update()
                break
            else:                   # select soilders / reset screen stack
                refreshWorld(screen, map_data, map_size)
                activeMenu["active"] = False
                break
    print(f"leftclick method: {time.time() - timeM}s")

def rightClickMenu(screen, map_data, map_size, MOUSE_POSITION, activeMenu):
    """
    Show tile info
    """
    timeM = time.time()
    fontMenu = pygame.font.SysFont("Consolas", 30)
    print(activeMenu)
    for index, tile in enumerate(map_data._tiles):
        if tile["polygon"].collidepoint(MOUSE_POSITION):
            menu = fontMenu.render(f"tile info {tile['status']}", True, (0, 0, 0))
            # screen.blit(activeMenu["menu"], MOUSE_POSITION)
            # map_data.updateMap(index, 1)
            # loadWorld(screen, map_data, map_size)
            if activeMenu["active"]:    # reset screen stack
                refreshWorld(screen, map_data, map_size)
                activeMenu["active"] = False
                break
            else:                       # push menu view on the screen stack
                activeMenu["menu"] = screen.blit(menu, MOUSE_POSITION)
                pygame.display.update()
                activeMenu["active"] = True
                break
    print(f"rightclick method: {time.time() - timeM}s")

# main

def main():
    screen = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption('Map Rendering Demo')
    FPSCLOCK = pygame.time.Clock()
    
    map_size = 50
    map_data = TileMap(map_size)

    loadWorld(screen, map_data, map_size)

    activeMenu = { "active": False, "menu": None }  # right click menu
    action = { "active": False }                    # left click actions
    scroll = [0, 0]                     # scroll screen controll

    pygame.display.flip()
    while True:
        MOUSE_POSITION = pygame.mouse.get_pos()
        pressedTile = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                                   # left click
                    leftClickAction(screen, map_data, map_size, MOUSE_POSITION, action, activeMenu)
                if event.button == 2:                                   # middle click
                    pass
                if event.button == 3:                                   # right click
                    rightClickMenu(screen, map_data, map_size, MOUSE_POSITION, activeMenu)
                if event.button == 4:                                   # mouse scroll top
                    pass
                if event.button == 5:                                   # mouse scroll down
                    pass
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                if key[pygame.K_UP]:
                    print(key[pygame.K_UP])
                    scroll[1] += 20
                    map_data = scrollMap(screen, map_data, scroll)
                if event.key == pygame.K_DOWN or key[pygame.K_DOWN]:
                    scroll[1] -= 20
                    map_data = scrollMap(screen, map_data, scroll)
                if event.key == pygame.K_RIGHT or key[pygame.K_RIGHT]:
                    scroll[0] -= 20
                    map_data = scrollMap(screen, map_data, scroll)
                if event.key == pygame.K_LEFT or key[pygame.K_LEFT]:
                    scroll[0] += 20
                    map_data = scrollMap(screen, map_data, scroll)
        FPSCLOCK.tick(30)

 
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    try:
        main()
    finally:
        pygame.quit()
