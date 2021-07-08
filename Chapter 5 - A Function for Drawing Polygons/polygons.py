# Import the Turtle Graphics module
import turtle


def draw_polygon(tur, num_sides, side_length):
    tur.begin_fill()
    for _ in range(num_sides):
        tur.forward(side_length)
        tur.right(360 / num_sides)
    tur.end_fill()


# Create a screen
screen = turtle.Screen()
screen.setup(500, 500)
screen.title("Turtle Polygons")
screen.bgcolor("red")

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("yellow")
my_turtle.width(2)  # Make the pen a bit thicker

# Move your turtle to where you want it to start drawing
my_turtle.penup()
my_turtle.goto(75, 175)
my_turtle.pendown()

# Draw a polygon
num_sides = 5
side_length = 100
draw_polygon(my_turtle, num_sides, side_length)

# And again
my_turtle.penup()
my_turtle.goto(-175, -50)
my_turtle.pendown()
num_sides = 9  # Nonagon
side_length = 50
draw_polygon(my_turtle, num_sides, side_length)

# Hide the turtle so we can admire our work
my_turtle.hideturtle()

# Finish nicely
turtle.done()
