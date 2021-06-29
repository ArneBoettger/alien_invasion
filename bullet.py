import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Bullet class'''

    def __init__(self, ai_game):
        #Python 3.x syntax, for Python 2.x: super(Bullet, self).__init__()
        super().__init__()
        self.screen = ai_game.screen

        #creates bullet at (0, 0), then update the position to top of ships position
        self.rect = pygame.Rect(0, 0, ai_game.settings.bullet_width, ai_game.settings.bullet_height)
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top
        #saves position as float
        self.y = float(self.rect.y)

        self.color = ai_game.settings.bullet_color
        self.speed = ai_game.settings.bullet_speed
    
    def update(self):
        #moves bullet up the screen
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        #draws bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)