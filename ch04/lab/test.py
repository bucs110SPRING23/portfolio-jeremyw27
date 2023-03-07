import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((600,600))
#screen.fill("black")
width,height = pygame.display.get_window_size()

hitboxes = {
    "green": pygame.Rect(0, 0, width/2, height),
    "blue": pygame.Rect(0, 0, width/2, height),
}

hitboxes["blue"].topleft = hitboxes["green"].topright

main_colors = {
 "green": (0, 200, 0),
 "blue": (0, 0, 200),
}
# Define highlight colors
highlight_colors = {
 "green": (0, 255, 0),
 "blue": (0, 0, 255),
}

pygame.draw.rect(screen, "green", hitboxes["green"])
pygame.display.flip()
pygame.draw.rect(screen, "blue", hitboxes["blue"])
pygame.display.flip()

font = pygame.font.Font(None, 30)
text = font.render("Select Green for P1 and Blue for P2!", True, "black")
screen.blit(text, (150, 300)) # where <x> and<y> are coordinates on screen
pygame.display.flip()
pygame.time.wait(2000)

done = False

yourguess = None

while not done:
    for event in pygame.event.get(): 
        #if event.type == pygame.MOUSEBUTTONDOWN:  # Click event
            #if event.button == 3:
                #print("Right mouse button pressed")
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["green"].collidepoint(event.pos):
                yourguess = 0
                done = True
            elif hitboxes["blue"].collidepoint(event.pos):
                yourguess = 1
                done = True

screen.fill("black")
pygame.draw.circle(screen, "white", (300,300), 300)
pygame.display.flip()
pygame.draw.line(screen, "black", (300,0), (300,600), width=2)
pygame.display.flip()
pygame.draw.line(screen, "black", (0,300), (600,300), width=2)
pygame.display.flip()

score1 = 0
score2 = 0

for i in range(10):
    # Player 1 is Green; Miss is red
    # Player 2 is Blue; Miss is yellow
    
    #Player 1
    x = random.randrange(0,600)
    y = random.randrange(0,600)
    x0 = 300
    y0 = 300
    width = 600

    distance_from_center = math.hypot(x-x0, y-y0) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width

    if is_in_circle == True:
        pygame.draw.circle(screen, "green", (x,y), 5)
        pygame.display.flip()
        score1 += 1
    elif is_in_circle == False:
        pygame.draw.circle(screen, "red", (x,y), 5)
        pygame.display.flip()
    
    #pygame.display.update()
    pygame.time.wait(250)    
    
    #Player 2
    x = random.randrange(0,600)
    y = random.randrange(0,600)
    x0 = 300
    y0 = 300
    width = 600

    distance_from_center = math.hypot(x-x0, y-y0) #the distance formula
    is_in_circle = distance_from_center <= width/2 #screen width

    
    if is_in_circle == True:
        pygame.draw.circle(screen, "blue", (x,y), 5)
        pygame.display.flip()
        score2 += 1
    elif is_in_circle == False:
        pygame.draw.circle(screen, "yellow", (x,y), 5)
        pygame.display.flip()
        
    #pygame.display.update()
    pygame.time.wait(250)

print(score1)
print(score2)

if score1 > score2:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 1 Wins!", True, "black")
    screen.blit(text, (300, 300)) # where <x> and<y> are coordinates on screen
    answer = 0
elif score2 > score1:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 2 Wins!", True, "black")
    screen.blit(text, (300, 300)) # where <x> and<y> are coordinates on screen
    answer = 1
elif score1 == score2:
    font = pygame.font.Font(None, 48)
    text = font.render("It is a Tie!", True, "black")
    screen.blit(text, (300, 300)) # where <x> and<y> are coordinates on screen
    answer = 2
    
if yourguess == answer:
    font = pygame.font.Font(None, 36)
    text = font.render("Your guess was correct!", True, "black")
    screen.blit(text, (300, 400)) # where <x> and<y> are coordinates on screen
elif yourguess != answer:
    font = pygame.font.Font(None, 36)
    text = font.render("Your guess was incorrect!", True, "black")
    screen.blit(text, (300, 350)) # where <x> and<y> are coordinates on screen

pygame.display.flip()
pygame.time.wait(1000)