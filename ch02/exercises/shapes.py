import pygame
pygame.init()

screen = pygame.display.set_mode()
screen.fill("lightblue")
pygame.display.flip()

screen_size = screen.get_size()

pygame.draw.circle(screen, "white", [screen_size[0] / 2, 200], 50)
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 280], 75)
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 390], 100)

pygame.display.flip()
pygame.time.wait(2000)