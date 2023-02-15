import turtle #1. import modules
import random
import pygame
import math
pygame.init()

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
#Race 1
michelangelo.forward(random.randrange(1, 101))
leonardo.forward(random.randrange(1, 101))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

#Race 2
for i in range(10):
   michelangelo.forward(random.randrange(1,11))
   leonardo.forward(random.randrange(1,11))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

window.exitonclick()



# PART B - complete part B here
window = pygame.display.set_mode()
window.fill("white")
pygame.display.flip()
screen_size = window.get_size()

xpos = screen_size[0] / 2
ypos = screen_size[1] / 2 - 250
side_length = 120

points = []
num_sides = 3
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "forestgreen", points)
pygame.display.flip()
pygame.time.wait(1500)
window.fill("lightblue")
pygame.display.flip()

points = []
num_sides = 4
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "magenta", points)
pygame.display.flip()
pygame.time.wait(1500)
window.fill("orange")
pygame.display.flip()

points = []
num_sides = 6
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "black", points)
pygame.display.flip()
pygame.time.wait(1500)
window.fill("blue")
pygame.display.flip()

points = []
num_sides = 20
side_length = 40
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "lightgreen", points)
pygame.display.flip()
pygame.time.wait(1500)
window.fill("yellow")
pygame.display.flip()

points = []
num_sides = 100
side_length = 12
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "red", points)
pygame.display.flip()
pygame.time.wait(1500)
window.fill("purple")
pygame.display.flip()

points = []
num_sides = 360
side_length = 4
for i in range(num_sides):
   angle = 360 / num_sides
   radians = math.radians(angle * i)
   xpos = xpos + side_length * math.cos(radians)
   ypos = ypos + side_length * math.sin(radians)
   points.append([xpos,ypos])
pygame.draw.polygon(window, "white", points)
pygame.display.flip()
pygame.time.wait(1500)