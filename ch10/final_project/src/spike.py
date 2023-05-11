import pygame
from src.utility import Utility

class Spike(pygame.sprite.Sprite):
    def __init__(self, image, index):
        """
        Instantiates spike object and scales it.
        args: image, index (There are several spike images; the index will indicate which image is selected.)
        return: none
        """
        super().__init__()
        self.index = index
        self.image = image[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = Utility.SCREEN_WIDTH
        self.rect.bottom = 426

    def update(self):
        """
        Removes the spike if it goes beyond the game bounds.
        args: none
        return: none
        """
        self.rect.x -= Utility.GAME_SPEED
        if self.rect.x <= -self.rect.width:
            self.kill()

    def draw(self, screen):
        """
        Draw the spike onto the screen.
        args: none
        return: none
        """
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, (255,0,0), self.rect, 3)

    # def shift_image(self, index):
    #     for _ in self.spike_height_1:
    #         if self.index == self.spike_height_1:
    #             self.rect.y - 
        