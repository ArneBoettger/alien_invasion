class Settings():
    '''A class to store all settings for Alien Invasion'''

    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 700

        #self.bg_color = (94, 4, 63) #uncomfortable purple
        #self.bg_color = (25, 48, 33) #disgusting dark green
        self.bg_color = (230, 230, 230)

        #ship settings
        self.ship_limit = 3

        #bullet settings
            #start settings: 3x15 bullets, speed same as ship, 3 max bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10
        #fleet_direction == 1 ~ to the right; -1 ~ to the left

        #game speedup
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        '''initializes settings throughout the game'''
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)