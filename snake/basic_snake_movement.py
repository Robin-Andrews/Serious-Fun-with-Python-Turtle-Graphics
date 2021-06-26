import turtle

WIDTH = 500
HEIGHT = 500


def draw_snake():
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()


def move_snake():
    stamper.clearstamps()  # Remove existing stamps made by stamper.
    new_head = snake[-1].copy()
    new_head[0] += 20
    snake.append(new_head)
    snake.pop(0)
    for segment in snake:
        stamper.goto(segment[0], segment[1])
        stamper.stamp()
    screen.update()
    turtle.ontimer(move_snake, 200)


# Screen
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)  # Disable automatic animation (mostly).

# Stamper Turtle
# This Turtle is defined at the global level, so is available to move_snake()
stamper = turtle.Turtle("square")
stamper.penup()

# Create snake as a list of coordinate pairs. This variable is available globally.
snake = [[0, 0], [20, 0], [40, 0], [60, 0]]

# Draw snake for the first time
draw_snake()

# Set animation in motion
move_snake()

# Finish nicely
turtle.done()
