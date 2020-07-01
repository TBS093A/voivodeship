import pygame
import time

from world import World

class Event(World):

    def __init__(self, gameWorld):
        super().__init__(gameWorld.screen, gameWorld.map_size)
        self.activeMenu = { "active": False, "menu": None }  # right click menu
        self.action = { "active": True }                    # left click actions
        self.scroll = [0, 0]                     # scroll screen controll

    def getTruePositionMousePosition(self, MOUSE_POSITION):
        print(self.scroll)
        print(MOUSE_POSITION)
        return (MOUSE_POSITION[0] - self.scroll[0], MOUSE_POSITION[1] - self.scroll[1])

    def leftClickAction(self, MOUSE_POSITION):
        timeM = time.time()
        MP_scroll = self.getTruePositionMousePosition(MOUSE_POSITION)
        for index, tile in enumerate(self.map_data._tiles):
            if tile["polygon"].collidepoint(MP_scroll):
                print(tile)
                if self.action["active"]:    # build
                    self.map_data.updateMap(index, 1)
                    self.refreshWorld(self.screen, self.scroll)
                    pygame.display.update()
                    break
                else:                   # select soilders / reset screen stack
                    self.refreshWorld(screen, self.scroll)
                    self.activeMenu["active"] = False
                    break
        print(f"leftclick method: {time.time() - timeM}s")
 
    def rightClickMenu(self, MOUSE_POSITION):
        """
        Show tile info
        """
        timeM = time.time()
        fontMenu = pygame.font.SysFont("Consolas", 30)
        print(self.activeMenu)
        MP_scroll = self.getTruePositionMousePosition(MOUSE_POSITION)
        print(MP_scroll)
        for index, tile in enumerate(self.map_data._tiles):
            if tile["polygon"].collidepoint(MP_scroll):
                menu = fontMenu.render(f"tile info {tile['status']}, index: {index}", True, (255, 0, 0))
                # screen.blit(activeMenu["menu"], MOUSE_POSITION)
                # map_data.updateMap(index, 1)
                # loadWorld(screen, map_data, map_size)
                print(tile)
                if self.activeMenu["active"]:    # reset screen stack
                    self.refreshWorld(self.screen, self.scroll)
                    self.activeMenu["active"] = False
                    break
                else:                       # push menu view on the screen stack
                    self.activeMenu["menu"] = self.screen.blit(menu, MOUSE_POSITION)
                    pygame.display.update()
                    self.activeMenu["active"] = True
                    break
        print(f"rightclick method: {time.time() - timeM}s")

    def worldScrollController(self, event, key):
        if event.key == pygame.K_UP or key[pygame.K_UP]:
            self.scroll[1] += 20
            self.scrollMap(self.screen, self.scroll)
        if event.key == pygame.K_DOWN or key[pygame.K_DOWN]:
            self.scroll[1] -= 20
            self.scrollMap(self.screen, self.scroll)
        if event.key == pygame.K_RIGHT or key[pygame.K_RIGHT]:
            self.scroll[0] -= 20
            self.scrollMap(self.screen, self.scroll)
        if event.key == pygame.K_LEFT or key[pygame.K_LEFT]:
            self.scroll[0] += 20
            self.scrollMap(self.screen, self.scroll)
