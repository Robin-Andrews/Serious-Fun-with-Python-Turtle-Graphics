"""
The Classic Snake Game with Python Turtle Graphics
Robin Andrews - https://compucademy.net/
"""
import turtle

WIDTH = 500
HEIGHT = 500

# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Disable automatic animation (mostly).

# Pen
pen = turtle.Turtle("square")

# Finish nicely
turtle.done()
