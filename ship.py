import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    '''Ship class'''
    
    def __init__(self, ai_game):
        '''initializes the ship and sets its positions'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #loads ship image and gets ship's screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        #places ship in the middle of the bottom screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #saves ship position as float, as ship_speed will also often be float 
        self.center = float(self.rect.centerx)

        #for continuous movement
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        #after changing position of ship: postion of rect-object gets updated as an integer
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''re-center ship after losing'''
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)