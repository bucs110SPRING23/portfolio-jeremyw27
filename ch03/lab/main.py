import pygame
import math
import random
pygame.init()

# Part A
screen = pygame.display.set_mode([600, 600])
screen_size = pygame.display.get_window_size()
screen.fill("lightblue")
pygame.display.flip()
pygame.draw.circle(screen, "black", [screen_size[0]/2, screen_size[1]/2], 300)
pygame.draw.circle(screen, "white", [screen_size[0]/2, screen_size[1]/2], 298)
pygame.display.flip()

#Part B
distance_from_center = math.hypot(x1-screen_size[0]/2, y1-screen_size[1]/2)
is_in_circle = distance_from_center <= screen_size[0]/2
for i in range(10):
    if is_in_circle == True:
        pygame.draw.circle(screen, "green", [random.randrange(screen_size[0]), random.randrange(screen_size[1])], 30)
    else:
        pygame.draw.circle(screen, "red", [random.randrange(screen_size[0]), random.randrange(screen_size[1])], 30)
    pygame.display.flip()

pygame.time.wait(2500)
print(random.randrange(screen_size[0]))