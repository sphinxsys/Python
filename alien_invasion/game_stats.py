
class GameStats:
    """ Track statistics for Alien Invasion. """

    def __init__(self, ai_game):
        """ Inistitalize statistics. """
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invation in an active state
        self.game_active = False
    
    def reset_stats(self):
        """ Initialize statistics that can change during the game. """
        self.ship_left = self.settings.ship_limit