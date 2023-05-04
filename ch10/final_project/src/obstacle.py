import pygame
import random
from src.block import Block
from src.spike import Spike
from src.cube import Cube
from src.background import Background

GAME_SPEED = 5
BLOCK = [pygame.image.load("assets/geometryblock1.png"),
         pygame.image.load("assets/geometryblock2.png"),
         pygame.image.load("assets/geometryblock3.png")]
SPIKE = [pygame.image.load("assets/spike1.png"),
         pygame.image.load("assets/spike2.png"),
         pygame.image.load("assets/spike3.png")]
DEATH_EFFECT = pygame.image.load("assets/death_effect.png")

class Obstacle:
    def __init__(self):
        pygame.init()
        self.index = random.randint(0,2)
        self.obstacles = pygame.sprite.Group()
        
        self.background = pygame.display.set_mode((1200, 500))
        self.width = self.background.get_width()
        self.death_effect = DEATH_EFFECT
    
    def update(self):
        if len(self.obstacles) == 0:
            if random.randint(0,1) == 0:
                self.obstacles.add(Block(BLOCK[0]))
            else:
                self.obstacles.add(Spike(SPIKE[2]))

        # for obstacle in self.obstacles:
        #     if not obstacle.rect.colliderect(Background().background.get_rect()):
        #         obstacle.kill()
        #     if obstacle.rect.colliderect(Cube().cube_rect):
        #         Cube().image = self.death_effect
        #         pygame.time.delay(2000)
    
    def draw(self, screen):
        # for obstacle in self.obstacles:
        #     screen.blit(obstacle, obstacle.rect)
        self.obstacles.draw(screen)
            

