import pygame
from pygame.locals import *
import sys
import time

from tileMap import TileMap
from world import World
from events import Event

# menu functionality class

class GeneralMenu:

    def __init__(self, screen):
        self.screenX = pygame.display.Info().current_w
        self.screenY = pygame.display.Info().current_h  
        self._menu = pygame.draw.rect(screen, 255, ((0,self.screenY), (self.screenX, -100)))

def main():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Twierdza - v0.0001')
    pygame.HWSURFACE    # enable GPU

    FPSCLOCK = pygame.time.Clock()
    
    map_size = 50
    gameWorld = World(screen, map_size)
    worldEvent = Event(gameWorld)

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
                    worldEvent.leftClickAction(MOUSE_POSITION)
                if event.button == 2:                                   # middle click
                    pass
                if event.button == 3:                                   # right click
                    worldEvent.rightClickMenu(MOUSE_POSITION)
                if event.button == 4:                                   # mouse scroll top
                    pass
                if event.button == 5:                                   # mouse scroll down
                    pass
            if event.type == pygame.KEYDOWN:
                key = pygame.key.get_pressed()
                worldEvent.worldScrollController(event, key)
        FPSCLOCK.tick(30)

 
if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    try:
        main()
    finally:
        pygame.quit()
