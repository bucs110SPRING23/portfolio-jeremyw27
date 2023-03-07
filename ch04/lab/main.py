import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode([600, 600])
width, height = pygame.display.get_window_size()

done = False
guess = []
winner = []

hitboxes = {
    "blue": pygame.Rect(0, 0, width/2, height),
    "forestgreen": pygame.Rect(0, 0, width/2, height),
}

hitboxes["forestgreen"].left = hitboxes["blue"].right

pygame.draw.rect(screen, "blue", hitboxes["blue"])
pygame.draw.rect(screen, "forestgreen", hitboxes["forestgreen"])
pygame.display.flip()

font = pygame.font.Font(None, 26)
text = font.render("Guess who will win: blue (P1) or green (P2)?", True, "black")
screen.blit(text, (width/4, height/2))
pygame.display.flip()
pygame.time.wait(150)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["blue"].collidepoint(event.pos):
                guess = 1
                done = True
            elif hitboxes["forestgreen"].collidepoint(event.pos):
                guess = 2
                done = True

screen.fill("lightblue")
pygame.display.flip()
pygame.draw.circle(screen, "black", [width/2, height/2], 300)
pygame.draw.circle(screen, "white", [width/2, height/2], 298)
pygame.draw.line(screen, "black", [300, 0], [300, 600], 2)
pygame.draw.line(screen, "black", [0, 300], [600, 300], 2)
pygame.display.flip()
player1 = 0
player2 = 0

for i in range(10):
    #Player 1's turn
    x = random.randrange(width+1)
    y = random.randrange(height+1)
    x0 = width/2
    y0 = height/2
    distance_from_center = math.hypot(x - x0, y - y0)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == True:
        pygame.draw.circle(screen, "blue", [x, y], 12) #player 1 is blue
        pygame.display.flip()
        player1 += 1
    else:
        pygame.draw.circle(screen, "red", [x, y], 12) #red is outside dartboard
        pygame.display.flip()
    pygame.time.wait(300)
    
    #Player 2's turn
    x = random.randrange(width+1)
    y = random.randrange(height+1)
    x0 = width/2
    y0 = height/2
    distance_from_center = math.hypot(x - x0, y - y0)
    is_in_circle = distance_from_center <= width/2
    if is_in_circle == True:
        pygame.draw.circle(screen, "forestgreen", [x, y], 12) #player 2 is green
        pygame.display.flip()
        player2 += 1
    else:
        pygame.draw.circle(screen, "orange", [x, y], 12) #orange is outside dartboard
        pygame.display.flip()
    pygame.time.wait(300)

print(player1)
print(player2)

pygame.time.wait(500)
font = pygame.font.Font(None, 48)
if player1 > player2:
    text = font.render("Player 1 wins! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (width/4, height/2))
    winner = 1
elif player1 < player2:
    text = font.render("Player 2 wins! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (width/4, height/2))
    winner = 2
else:
    text = font.render("It's a tie! Score: " + str(player1) + "-" + str(player2), True, "black")
    screen.blit(text, (width/4, height/2))

if guess == winner:
    text = font.render("Your guess was correct!", True, "black")
    screen.blit(text, (width/4, 350))
else:
    text = font.render("Your guess was incorrect!", True, "black")
    screen.blit(text, (width/4, 350))
pygame.display.flip()
pygame.time.wait(2500)