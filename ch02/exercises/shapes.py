import pygame
pygame.init()

screen = pygame.display.set_mode()
screen.fill("lightblue")
pygame.display.flip()

screen_size = screen.get_size()

pygame.draw.circle(screen, "black", [screen_size[0] / 2, 405], 102)
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 405], 100)
pygame.draw.circle(screen, "black", [screen_size[0] / 2, 280], 77)
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 280], 75)
pygame.draw.circle(screen, "black", [screen_size[0] / 2, 180], 52)
pygame.draw.circle(screen, "white", [screen_size[0] / 2, 180], 50)

pygame.display.flip()
pygame.time.wait(2000)