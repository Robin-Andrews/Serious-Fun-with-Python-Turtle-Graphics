import turtle


def draw_circle(tur, x, y, radius, color="black"):
    """
    Draws a circle with center at (x, y), radius radius and color color.
    Create your turtle elsewhere and pass it in as tur.
    """
    tur.color(color)
    tur.pu()
    tur.goto(x, y - radius)  # -radius because the default circle method starts drawing at the border.
    tur.pd()
    tur.begin_fill()
    tur.circle(radius)
    tur.end_fill()


# Set up screen
screen = turtle.Screen()
screen.title("Archery")
screen.setup(450, 450)
screen.bgcolor("cyan")

# Draw the target
toby = turtle.Turtle()
toby.speed(0)
toby.width(5)
toby.hideturtle()

draw_circle(toby, 0, 0, 160, "black")  # Draw a black circle at coords (0, 0) with radius 160 pixels
draw_circle(toby, 0, 0, 120, "blue")
draw_circle(toby, 0, 0, 80, "red")
draw_circle(toby, 0, 0, 40, "yellow")

# Make it all work properly
turtle.done()
