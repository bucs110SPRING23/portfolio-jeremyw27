import turtle
import random

screen = turtle.Screen()
turtle1 = turtle.Turtle()
x = screen.screensize([0])
y = screen.screensize([1])
print(x)
turtle1.goto(int(x)/2,int(y)/2)

if random.randrange(2) == 0:
    turtle1.left(90)
elif random.randrange(2) == 1:
    turtle1.right(90)
