import pygame
from src.utility import Utility

class Score:
    def __init__(self):
        """
        Creates a point system for the player through text on the screen. Custom font imported.
        args: none
        return: none
        """
        self.points = 0
        self.text = Utility.FONT.render("Points: " + str(self.points), True, "orange")
        self.text_rect = self.text.get_rect(center = (600, 70))
    
    def update(self):
        """
        Updates the score. For every 100 points added to the score, the game speed will increase by 0.2.
        args: none
        return: none
        """
        self.text = Utility.FONT.render("Score: " + str(self.points), True, "orange")
        self.points += 1
        if self.points % 100 == 0:
            Utility.GAME_SPEED += 0.2
    
    def end_screen_score(self):
        self.text = Utility.FONT.render("Your Final Score: " + str(self.points), True, "orange")

    def draw(self, screen):
        """
        Display the text on the screen.
        args: none
        return: none
        """
        screen.blit(self.text, self.text_rect)

    
    #def game_speed(self):
        #self.speed = GAME_SPEED