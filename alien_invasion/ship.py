import os
import pygame

class Ship():
    """ A class to manage the ship. """

    def __init__(self, ai_game):
        """ Initialize the ship and start its starting position. """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load space ship image
        path = os.path.join("images", "ship.bmp")
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect()

        # Start a new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
    
    def blitme(self):
        """ Draw the sapce ship at its current postion. """
        self.screen.blit(self.image, self.rect)