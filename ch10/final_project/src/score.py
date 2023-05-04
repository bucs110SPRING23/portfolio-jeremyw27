import pygame

GAME_SPEED = 5
TEXT_POS_X = 600
TEXT_POS_Y = 70
FONT_SIZE = 28

class Score:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('assets/pusab_ttf.ttf', FONT_SIZE)
        self.speed = GAME_SPEED
        self.points = 0

        self.text = self.font.render("Points: " + str(self.points), True, "orange")
        self.text_rect = self.text.get_rect(center = (TEXT_POS_X, TEXT_POS_Y))
    
    def update(self):
        self.text = self.font.render("Points: " + str(self.points), True, "orange")
        
        self.points += 1
        if self.points % 100 == 0:
            self.speed += 1
    
    def draw(self, screen):
        screen.blit(self.text, self.text_rect)

    #def game_speed(self):
        #self.speed = GAME_SPEED