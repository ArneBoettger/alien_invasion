import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
    def __init__(self):
        #initializes pygame and loads settings
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #loads ship
        self.ship = Ship(self.settings, self.screen)
        #creates group to save bullets
        self.bullets = Group()
        #create alien fleet
        self.aliens = Group()
        gf._create_fleet(self.settings, self.screen, self.ship, self.aliens)

    def run_game(self):
        while True:
            #checks for events and updates ship, bullets and rest of the screen
            gf._check_events(self.settings, self.screen, self.ship, self.bullets)
            self.ship.update()
            gf._update_bullets(self.settings, self.screen, self.ship, self.bullets, self.aliens)
            gf._update_aliens(self.aliens, self.settings)
            gf._update_screen(self.settings, self.screen, self.ship, self.bullets, self.aliens)

            #updates of the entire display
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()