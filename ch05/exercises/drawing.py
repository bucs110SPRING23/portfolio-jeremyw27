import turtle

def draw_eq_shape(turtle, sides, length):
    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360/sides)
    window.exitonclick()

window = turtle.Screen()
t = turtle.Turtle()
t.shape("turtle")
t.color("green")

num_sides = int(input("How many sides do you want in your shape? "))
side_length = int(input("How long do you want each side to be? "))

draw_eq_shape(t, num_sides, side_length)