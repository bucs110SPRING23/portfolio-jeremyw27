import turtle

#drawing flower center
def flower_center(center_radius=0, center_color=" "):
    '''
    This function is to draw the center of the flower with a color that the user inputs.
    The radius of the center is calculated by dividing the radius of the petal by 3.
    args: radius of center (int) and color of center (str)
    return: None
    '''
    pen.fillcolor(center_color)
    pen.begin_fill()
    pen.circle(center_radius) #drawing the flower center with the calculated radius using the petals
    pen.end_fill()

#drawing flower petals
def flower_petal(flower_color=" ", petal_size=0):
    '''
    This function is to draw a flower with six petals using the color that the user inputs.
    The size of the petals and thus the flower is determined by user input.
    args: color of flower (str) and size/radius of petals (int)
    return: x and y coordinates of the turtle/pen (tuple)
    '''
    x_cor, y_cor = pen.position()
    pen.setheading(0)
    pen.fillcolor(flower_color)
    pen.begin_fill()
    petals = 6
    for _ in range(petals):
        pen.circle(petal_size, 120) #drawing half of one petal
        pen.left(60)
        pen.circle(petal_size, 120) #finishing the other half of the petal
    pen.end_fill()
    return x_cor, y_cor

def main():
    flower_color = str(input("What color do you want your flower?: "))
    center_color = str(input("What color do you want the center of your flower?: "))
    petal_size = int(input("How big do you want your flower (enter a number)?: "))
    center_radius = petal_size/3 #radius of center is a third of the radius of the petal

    x_cor, y_cor = flower_petal(flower_color, petal_size)
    pen.up()
    pen.goto(x_cor, y_cor-center_radius) #to center the flower center, move down the y-axis by the center radius
    pen.down()
    flower_center(center_radius, center_color)

#initialize turtle and screen
pen = turtle.Turtle()
pen.speed(10)
window = turtle.Screen()
window.bgcolor("lightblue")

main()

window.exitonclick()