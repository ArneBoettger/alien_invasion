class Settings():
    '''A class to store all settings for Alien Invasion'''

    def __init__(self) -> None:
        self.screen_width = 1200
        self.screen_height = 700

        #self.bg_color = (94, 4, 63) #uncomfortable purple
        #self.bg_color = (25, 48, 33) #disgusting dark green
        self.bg_color = (230, 230, 230)

        #ships's speed
        self.ship_speed_factor = 1.5

        #bullet settings
            #start settings: 3x15 bullets, 2/3 speed of ship, max bullets
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #alien speed
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction == 1 ~ to the right; -1 ~ to the left
        self.fleet_direction = 1