import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        '''initializes button attributes'''
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #size and functionality of the button
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #creates rect-object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #button text
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''turns msg into rendered image and centers the text on the button'''
        #antialias on
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''draws empty button, then adds text'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)