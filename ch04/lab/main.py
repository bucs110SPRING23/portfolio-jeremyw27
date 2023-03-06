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
player1 = 0
player2 = 0

for i in range(10):
    xcor = random.randrange(screen_size[0]+1)
    ycor = random.randrange(screen_size[1]+1)
    distance_from_center = math.hypot(xcor - screen_size[0]/2, ycor - screen_size[1]/2)
    if distance_from_center <= screen_size[0]/2:
        pygame.draw.circle(screen, "orange", [xcor, ycor], 12) #player 1 is orange
        pygame.display.flip()
        pygame.time.wait(400)
        player1 += 1
    else:
        pygame.draw.circle(screen, "red", [xcor, ycor], 12) #red is outside the dartboard
        pygame.display.flip()
        pygame.time.wait(400)
    xcor = random.randrange(screen_size[0]+1)
    ycor = random.randrange(screen_size[1]+1)
    if distance_from_center <= screen_size[0]/2:
        pygame.draw.circle(screen, "blue", [xcor, ycor], 12) #player 2 is blue
        pygame.display.flip()
        pygame.time.wait(400)
        player2 += 1
    else:
        pygame.draw.circle(screen, "red", [xcor, ycor], 12) #red is outside the dartboard
        pygame.display.flip()
        pygame.time.wait(400)

print(player1)
print(player2)
font = pygame.font.Font(None, 48)

if player1 > player2:
    text = font.render("Player 1 wins the game! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (screen_size[0]/2, screen_size[1]/2))
elif player1 < player2:
    text = font.render("Player 2 wins the game! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (screen_size[0]/2, screen_size[1]/2))
else:
    text = font.render("It's a tie! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (screen_size[0]/2, screen_size[1]/2))

pygame.time.wait(1200)