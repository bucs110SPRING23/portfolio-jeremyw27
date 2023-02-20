import pygame
pygame.init()
screen = pygame.display.set_mode()
screen_size = pygame.display.get_window_size()
screen.fill("lightblue")
pygame.display.flip()
pygame.time.wait(1500)