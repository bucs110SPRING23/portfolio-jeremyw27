import turtle
sides = int(input("Enter a number of sides: "))
length = int(input("Enter length of each side: "))

pen = turtle.Turtle()
window = turtle.Screen()
pen.color('green')

for i in range(sides):
   pen.forward(length)
   pen.left(360/sides)

window.exitonclick()