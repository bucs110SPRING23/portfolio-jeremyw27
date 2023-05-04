import pygame
import random
from src.score import GAME_SPEED

SPIKE_POS_Y = 362
SPIKE_SCALE = 60

class Spike(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()

        self.width, self.height = pygame.display.get_window_size()
        self.image = pygame.transform.scale(image, (SPIKE_SCALE, SPIKE_SCALE))
        self.rect = self.image.get_rect()
        self.rect.x = self.width
        self.rect.y = SPIKE_POS_Y

    def update(self):
        self.rect.x -= GAME_SPEED
        if self.rect.x <= -self.rect.width:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)
        