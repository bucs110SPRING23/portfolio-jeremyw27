import pygame
import random
from src.utility import Utility

class Block(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.width, self.height = pygame.display.get_window_size()
        self.image = pygame.transform.scale(image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.width
        self.rect.y = 362

    def update(self):
        self.rect.x -= Utility.speed
        if self.rect.x <= -self.rect.width:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
