import pygame
from src.utility import Utility

class Background:
    def __init__(self, img="assets/background.png"):
        """
        Creates the background and scales it reasonably.
        args: none
        return: none
        """

        # position of background
        self.bg_x = 0
        self.bg_y = 0

        # creating the background itself
        self.image = pygame.image.load(img)
        self.screen = pygame.display.set_mode((Utility.SCREEN_WIDTH, Utility.SCREEN_HEIGHT))
        self.background = pygame.transform.smoothscale(self.image, self.screen.get_size())
        

    def update(self):
        """
        Moves the background across the screen; when it moves off screen, a new one is constantly created to loop the background.
        args: none
        return: none
        """
        self.screen.blit(self.background, (self.bg_x, self.bg_y))
        self.screen.blit(self.background, (Utility.SCREEN_WIDTH + self.bg_x, self.bg_y))
        if self.bg_x <= -Utility.SCREEN_WIDTH:
            self.screen.blit(self.background, (Utility.SCREEN_WIDTH + self.bg_x, self.bg_y))
            self.bg_x = 0
        self.bg_x -= Utility.GAME_SPEED

    def get_screen(self):
        """
        Function to return the size of the screen.
        args: none
        return: tuple
        """
        return self.screen