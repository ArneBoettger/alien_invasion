import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        #Python 3.x syntax, for Python 2.x: super(Bullet, self).__init__()
        super().__init__()
        self.screen = screen

        #creates bullet at (0, 0), then update the position to top of ships position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #saves position as float
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    
    def update(self):
        #moves bullet up the screen
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        #draws bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)