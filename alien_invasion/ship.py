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

        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """ Update the ship's position based on the movement flag. """
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
    
    def blitme(self):
        """ Draw the sapce ship at its current postion. """
        self.screen.blit(self.image, self.rect)