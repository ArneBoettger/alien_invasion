import pygame
from pygame.sprite import Group

import game_functions as gf
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:

    def __init__(self):
        #initializes pygame and loads settings
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        #creates GameStats instance to save statistics and a scoreboard to show score
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        #loads ship
        self.ship = Ship(self) 
        #creates group to save bullets
        self.bullets = Group()
        #create alien fleet
        self.aliens = Group()
        gf._create_fleet(self)
        #create play-button
        self.play_button = Button(self, "Play")

    def run_game(self):
        while True:
            #checks for events and updates ship, bullets and rest of the screen
            gf._check_events(self)

            if self.stats.game_active:
                self.ship.update()
                gf._update_bullets(self)
                gf._update_aliens(self)
            gf._update_screen(self)

            #updates of the entire display
            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()