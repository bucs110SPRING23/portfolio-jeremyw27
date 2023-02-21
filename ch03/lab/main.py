import pygame
pygame.init()

# Part A
screen = pygame.display.set_mode([600, 600])
screen_size = pygame.display.get_window_size()
screen.fill("lightblue")
pygame.display.flip()
pygame.draw.circle(screen, "black", [screen_size[0]/2, screen_size[1]/2], 300)
pygame.draw.circle(screen, "red", [screen_size[0]/2, screen_size[1]/2], 298)
pygame.display.flip()
pygame.time.wait(2500)

#Part B
