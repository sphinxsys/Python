import pygame

class Ship():
    """ A class to make space ship object. """

    def __init__(self, screen):
        """ Initialize the ship and start its starting position. """
        self.screen = screen

        # Load space ship image
        self.image = pygame.image.load("D:\\Workspace\\Python\\alien_invasion\\images\\ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start a new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    
    def blitme(self):
        """ Draw the sapce ship at its current postion. """
        self.screen.blit(self.image, self.rect)