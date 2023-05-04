import pygame
from src.cube import Cube
from src.score import Score
from src.background import Background, SCREEN_WIDTH, SCREEN_HEIGHT
from src.obstacle import Obstacle

FPS = 60

class Controller:
    def __init__(self):
        pygame.init()

        # initializing instance variables
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # fix using background
        
        self.clock = pygame.time.Clock()
        self.player = Cube()
        self.score = Score()
        self.move_bg = Background()
        self.obstacles = Obstacle()

    def gameloop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False

            # make background move
            self.move_bg.update()

            # allow cube to jump
            key_press = pygame.key.get_pressed()
            self.player.draw(self.screen)
            self.player.update(key_press)

            # obstacles
            self.obstacles.update()
            #self.obstacles.draw(self.screen)

            # update score
            self.score.draw(self.screen)
            self.score.update()
            
            # frame rate
            self.clock.tick(FPS)
            
            
            

            pygame.display.update()

            

    def endloop():
        pass