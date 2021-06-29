import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''Class for a single alien ship'''
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings

        #loads alien ship image and defines rect-attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #position in upper left corner of the screen, saves position as float
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def update(self):
        '''moves alien ships'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        '''True if at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True