class Settings():
    """ A class to store all settings for alien invasion game"""

    def __init__(self):
        """ Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # ship settings
        # movement speed
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 1
        # fleet_direct of 1 represents right; -1 represents left.
        self.fleet_direction = 1
