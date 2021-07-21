# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Stamping")
screen.bgcolor("cyan")

# Create a turtle to do your bidding
stamper = turtle.Turtle()
stamper.color("red")
stamper.shape("square")
stamper.shapesize(50 / 20)  # Trust me on this one. Just take the size you want and / by 20.
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)  # Trust me on this one. Just take the size you want and / by 20.
stamper.goto(100, 100)
stamper.stamp()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
