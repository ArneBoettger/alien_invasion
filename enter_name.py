import pygame.font

class EnterNameTextField:
    '''class for entering name if a new high score is achieved'''

    def __init__(self, ai_game, msg):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #temporal name field
        self.temp_name = []

        #size and font of message
        self.width, self.height = 400, 120
        self.tf_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        #creates rect-object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        #prepate message
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''turns msg into rendered image'''
        self.line1_image = self.font.render(msg, True, self.text_color, self.tf_color)
        self.line2_image = self.font.render("Enter Name: ", True, self.text_color, self.tf_color)

    def draw_textfield(self, ai_game):
        '''draw new enter-name textfield'''
        self.screen.fill(self.tf_color, self.rect)
        self.screen.blit(self.line1_image, pygame.Rect(462, 313, 277, 35))
        self.screen.blit(self.line2_image, pygame.Rect(462, 358, 208, 33))