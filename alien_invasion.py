import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #initializes pygame and loads settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #loads ship
    ship = Ship(ai_settings, screen)
    #creates group to save bullets
    bullets = Group()

    while True:
        #checks for events and updates ship, bullets and rest of the screen
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ship, bullets)

        #updates of the entire display
        pygame.display.flip()

run_game()