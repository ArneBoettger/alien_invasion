import pygame

class Ship():
    '''Ship class'''
    def __init__(self, settings, screen) -> None:
        self.screen = screen
        self.settings = settings

        #loads ship image and gets ship's screen
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #places ship in the middle of the bottom screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #saves ship position as float, as ship_speed_factor will also often be float 
        self.center = float(self.rect.centerx)

        #for continuous movement
        self.moving_left = False
        self.moving_right = False
    
    def update(self):
        #after changing position of ship: postion of rect-object gets updated as an integer
        if self.moving_left and self.rect.left > 0:
            self.center -= self.settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.settings.ship_speed_factor
        self.rect.centerx = self.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)