import pygame
from src.score import Score

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
BG_POS_X = 0
BG_POS_Y = 0
GAME_SPEED = 5

class Background:
    def __init__(self, img="assets/background.png"):
        pygame.init()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.bg_x = BG_POS_X
        self.bg_y = BG_POS_Y

        self.image = pygame.image.load(img)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.transform.smoothscale(self.image, self.screen.get_size())
        

    def update(self):
        self.screen.blit(self.background, (self.bg_x, self.bg_y))
        self.screen.blit(self.background, (self.width + self.bg_x, self.bg_y))
        if self.bg_x <= -self.width:
            self.screen.blit(self.background, (self.width + self.bg_x, self.bg_y))
            self.bg_x = 0
        self.bg_x -= GAME_SPEED

    #def screen_size(self):
        #return self.screen

    #def width(self) -> int:
        #return SCREEN_WIDTH

    #def height(self) -> int:
        #return SCREEN_HEIGHT