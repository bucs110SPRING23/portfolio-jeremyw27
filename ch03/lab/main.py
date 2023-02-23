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
pygame.draw.line(screen, "black", [300, 0], [300, 600], 2)
pygame.draw.line(screen, "black", [0, 300], [600, 300], 2)
pygame.display.flip()

#Part B
for i in range(10):
    xcor = random.randrange(screen_size[0]+1)
    ycor = random.randrange(screen_size[1]+1)
    distance_from_center = math.hypot(xcor - screen_size[0]/2, ycor - screen_size[1]/2)
    is_in_circle = distance_from_center <= screen_size[0]/2
    if is_in_circle == True:
        pygame.draw.circle(screen, "green", [xcor, ycor], 15) #green is inside dartboard
        pygame.time.wait(300)
        print(xcor, ycor, distance_from_center)
    else:
        pygame.draw.circle(screen, "red", [xcor, ycor], 15) #red is outside dartboard
        pygame.time.wait(300)
        print(xcor, ycor, distance_from_center)
    pygame.display.flip()
pygame.time.wait(1200)