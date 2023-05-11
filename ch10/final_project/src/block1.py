import pygame
import random
from src.background import Background
from src.score import Score

BLOCK_POS_Y = 362

class Block:
    def __init__(self, image, type):
        pygame.init()

        self.width = Background().screen.get_width()
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = self.width

        self.type = random.randint(1,3)
        self.rect.y = BLOCK_POS_Y

    def update(self):
        self.rect.x -= Score().speed
        if self.rect.x <= -self.rect.width:
            obstacles.pop()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
