# Import the Turtle Graphics module
import turtle

# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(500, 500)  # Set the dimensions of the Turtle Graphics window.
screen.title("Colourful Spiral")
screen.bgcolor("black")

# Create a turtle called myrtle (with a lower case "m").
myrtle = turtle.Turtle()
myrtle.speed(10)  # Fastest possible speed.
myrtle.width(3)  # The width of myrtle's pen.

# Define some colours for our drawing
colors = ["purple", "cyan", "green"]

# Make a loop - it will run 100 times.
for i in range(100):
    # Cycle through the colours ("%" is the magic key).
    myrtle.pencolor(colors[i % 3])
    # Move myrtle forward by an amount related to the loop counter.
    myrtle.forward(i * 2)
    # Rotate myrtle just less than 60% so we get the spiral effect.
    myrtle.right(60)

# Hide myrtle now her work is done.
myrtle.hideturtle()

# This statement (or an equivalent) is needed at the end of all your turtle programs.
turtle.done()
