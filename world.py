import pygame
import time

from tileMap import TileMap

class World:

    TILEWIDTH = 64  #holds the tile width and height
    TILEHEIGHT = 64
    TILEHEIGHT_HALF = TILEHEIGHT /2
    TILEWIDTH_HALF = TILEWIDTH /2

    def __init__(self, screen, size):
        self.map_data = TileMap(size)
        self.map_size = size
        self.screenX = pygame.display.Info().current_w
        self.screenY = pygame.display.Info().current_h
        self.wall = pygame.image.load('wall.png').convert_alpha()
        self.grass = pygame.image.load('grass.png').convert_alpha()
        self.screen = screen
        self.loadWorld(screen)

    def scrollMap(self, screen, scroll):
        timeM = time.time()
        pygame.draw.rect(screen, 0, ((0,self.screenY), (self.screenX, -self.screenY)))  # mask
        for row_nb, row in enumerate(self.map_data):
            for col_nb, tile in enumerate(row):
                if tile == 1:
                    tileImage = self.wall
                else:
                    tileImage = self.grass

                cart_x = row_nb * self.TILEWIDTH_HALF
                cart_y = col_nb * self.TILEHEIGHT_HALF  
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                
                centered_x = screen.get_rect().centerx + iso_x + scroll[0]
                centered_y = screen.get_rect().centery/2 + iso_y + scroll[1]

                top = (centered_x, centered_y + 16)
                left = (centered_x - 32, centered_y)
                bottom = (centered_x, centered_y - 16)
                right = (centered_x + 32, centered_y)
                position = { "top": top, "right": right, "bottom": bottom, "left": left}

                polygon = pygame.draw.polygon(screen, 255, (top, right, bottom, left))
                if ( top[0] < self.screenX or right[0] < self.screenX or left[0] < self.screenX or bottom[0] < self.screenX ):
                    self.map_data.appendTile(polygon, position)
                screen.blit(tileImage, (centered_x - 32, centered_y - 47))
        pygame.display.update()
        print(f"scrollmap method: {time.time() - timeM}s")


    def loadWorld(self, screen):
        """
        Create new world map
        """
        timeM = time.time()
        
        for row_nb, row in enumerate(self.map_data):    #for every row of the map...
            for col_nb, tile in enumerate(row):
                if tile == 1:
                    tileImage = self.wall
                else:
                    tileImage = self.grass
                cart_x = row_nb * self.TILEWIDTH_HALF
                cart_y = col_nb * self.TILEHEIGHT_HALF  
                iso_x = (cart_x - cart_y) 
                iso_y = (cart_x + cart_y)/2
                
                centered_x = screen.get_rect().centerx + iso_x
                centered_y = screen.get_rect().centery/2 + iso_y

                top = (centered_x, centered_y + 16)
                left = (centered_x - 32, centered_y)
                bottom = (centered_x, centered_y - 16)
                right = (centered_x + 32, centered_y)
                position = { "top": top, "right": right, "bottom": bottom, "left": left}

                polygon = pygame.draw.polygon(screen, 255, (top, right, bottom, left))
                if ( top[0] < self.screenX or right[0] < self.screenX or left[0] < self.screenX or bottom[0] < self.screenX ):
                    self.map_data.appendTile(polygon, position)
                screen.blit(tileImage, (centered_x - 32, centered_y - 47))
        print(f"loadworld method: {time.time() - timeM}s")

    def refreshWorld(self, screen, scroll):
        """
        Clear screen (hide open menus itp)
        """
        timeM = time.time()
        self.scrollMap(screen, scroll) # refresh world
        pygame.display.update()
        print(f"refreshworld method: {time.time() - timeM}s")