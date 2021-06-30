# Import the Turtle Graphics module
import turtle


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, 10)  # After 100 milliseconds, call move_turtle() again.


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(500, 500)  # Set the dimensions of the Turtle Graphics window.
screen.title("Turtle Animation")
screen.bgcolor("cyan")

# Create a turtle to do your bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Turn off automatic animation
screen.tracer(0)


move_turtle()

turtle.done()
