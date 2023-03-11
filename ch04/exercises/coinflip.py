import turtle
import random

window = turtle.Screen()
turtle1 = turtle.Turtle()
inside_window = True

while inside_window:
    coinflip = random.randrange(0,2)
    if coinflip == 0: #heads
        turtle1.left(90)
    else: #tails
        turtle1.right(90)
    turtle1.forward(50)
    
    turtle_xcor = window.window_width()/2
    turtle_ycor = window.window_height()/2
    if abs(turtle1.xcor()) > turtle_xcor or abs(turtle1.ycor()) > turtle_ycor:
        inside_window = False

window.exitonclick()