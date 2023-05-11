import pygame
import pygame_menu
import random
from src.cube import Cube
from src.score import Score
from src.background import Background
from src.spike import Spike
from src.utility import Utility

class Controller:
    def __init__(self):
        """
        
        """
        # creating instance variables
        self.clock = pygame.time.Clock()
        self.player = Cube()
        self.score = Score()
        self.move_bg = Background()
        self.screen = self.move_bg.get_screen()

        # make sprite group
        self.index = random.randint(0,5)
        self.spikes = pygame.sprite.Group()
        self.spike_images = [pygame.transform.scale(pygame.image.load("assets/spike1.png"), (37.5, 37.5)),
                               pygame.transform.scale(pygame.image.load("assets/spike2.png"), (75, 37.5)),
                               pygame.transform.scale(pygame.image.load("assets/spike3.png"), (112.5, 37.5)),
                               pygame.transform.scale(pygame.image.load("assets/spike4.png"), (37.5, 75)),
                               pygame.transform.scale(pygame.image.load("assets/spike5.png"), (75, 75)),
                               pygame.transform.scale(pygame.image.load("assets/spike6.png"), (37.5, 112.5))]
        self.spikes.add(Spike(self.spike_images, self.index))

        self.death_count = 0
        self.restart_text = Utility.FONT.render("Press any Key to Quit Game", True, "orange")
        self.restart_text_rect = self.restart_text.get_rect(center = (600, 200))

        self.state = "START"
        self.about_menu = pygame_menu.Menu("About", Utility.SCREEN_WIDTH, Utility.SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        self.main_menu = pygame_menu.Menu("Geometry Dash", Utility.SCREEN_WIDTH, Utility.SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        self.game_over_menu = pygame_menu.Menu("Game Over", Utility.SCREEN_WIDTH, Utility.SCREEN_HEIGHT, theme=pygame_menu.themes.THEME_BLUE)
        # add buttons to each menu
        self.about_menu.add.button("Return to Main Menu", pygame_menu.events.BACK)
        self.main_menu.add.button("Play!", self.startloop)
        self.main_menu.add.button("About", self.about_menu)
        self.main_menu.add.button("Exit Game", pygame_menu.events.EXIT)
        self.game_over_menu.add.button("Play Again", self.gameloop)
        self.game_over_menu.add.button("Return to Main Menu", self.main_menu)
        self.game_over_menu.add.button("Exit Game", pygame_menu.events.EXIT)

    def mainloop(self):
        """
        """
        while True:
            if self.state == "GAME":
                self.gameloop()
            elif self.state == "START":
                self.menuloop()
            elif self.state == "END":
                self.endloop()
    
    def startloop(self):
        self.state = "GAME"
        
    def menuloop(self):
        """
        """
        while self.state == "START":
            if self.main_menu.is_enabled():
                self.main_menu.update(pygame.event.get())
                self.main_menu.draw(self.screen)
            pygame.display.update()

            # if self.death_count == 0:
            #     Utility.FONT.render("Click o")
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()
            #         self.running = False

    def gameloop(self):
        """
        """
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # make background move
            self.move_bg.update()

            # allow cube to jump
            key_press = pygame.key.get_pressed()
            self.player.update(key_press)

            # managing spikes and collisions
            for spike in self.spikes:
                spike.update()
                spike.draw(self.screen)
            
            if len(self.spikes) == 0:
                self.index = random.randint(0,5)
                self.spikes.add(Spike(self.spike_images, self.index))
            
            result = pygame.sprite.spritecollide(self.player, self.spikes, False)
            if len(result) > 0:
                self.player.death()
                self.endloop()
            
            self.player.draw(self.screen)

            # update score
            self.score.update()
            self.score.draw(self.screen)
            
            # frame rate
            self.clock.tick(60)
            
            pygame.display.update()

    def endloop(self):
        """
        """
        run = True
        while run:
            self.score.end_screen_score()
            self.screen.blit(self.restart_text, self.restart_text_rect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    run = False
            # if self.game_over_menu.is_enabled():
            #     self.game_over_menu.update(pygame.event.get())
            #     self.game_over_menu.draw(self.screen)
            # pygame.display.update()