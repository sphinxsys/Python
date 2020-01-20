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

        # Bullet settings
        self.bullet_speed = 0.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)