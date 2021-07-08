import turtle
import random

try:
    import playsound  # Not part of standard Library.

    SOUND = True
except ImportError:
    SOUND = False

WIDTH = 500
HEIGHT = 400
CURSOR_SIZE = 20
SQUARE_SIZE = 50
NUM_ROWS = 5
NUM_COLS = 5
BG_COLOR = "yellow"
TITLE = "Arachnophobia"
COLORS = ("red", "black")
SPEED = 500
NUM_TRIES = 20


def init_screen():
    screen = turtle.Screen()
    screen.title(TITLE)
    screen.setup(WIDTH, HEIGHT)
    canvas = screen.getcanvas()
    return screen, canvas


def create_board():
    board = []
    for i in range(NUM_ROWS):
        for j in range(NUM_COLS):
            tur = turtle.Turtle(shape="square")
            tur.setheading(90)
            board.append(tur)
            tur.penup()
            tur.shapesize(SQUARE_SIZE / CURSOR_SIZE)
            tur.color(COLORS[0] if i % 2 == j % 2 else COLORS[1])
            tur.onclick(lambda x, y, tur=tur: click(tur))
            x = -NUM_COLS / 2 * SQUARE_SIZE + j * SQUARE_SIZE + SQUARE_SIZE / 2
            y = NUM_ROWS / 2 * SQUARE_SIZE - i * SQUARE_SIZE - SQUARE_SIZE / 2
            tur.goto(x, y)
    return board


def click(tur):
    global score, high_score  # These values are modified within this function.
    if board.index(tur) == spider_pos:
        if SOUND:
            playsound.playsound("ouch2.mp3", False)
        score += 1
        if score > high_score:
            high_score = score
        update_score()


def toggle_turtle(tur):
    if tur.shape() == "square":
        tur.shape("spider.gif")
    else:
        tur.shape("square")
    # Turtles lose their onclick binding when image is used, so we have to rebind.
    tur.onclick(lambda x, y, tur=tur: click(tur))
    screen.update()


def update_score():
    pen.clear()
    pen.write(f"Score: {score}    High Score: {high_score}", font=("Arial", 16, "bold"))


def reset():
    global spider_pos, pen, score, high_score, board, counter

    # Reset screen
    screen.clear()
    screen.bgcolor(BG_COLOR)
    screen.register_shape("spider.gif")
    screen.tracer(0)  # Disable animation

    # Initialise board
    board = create_board()
    spider_pos = 0
    toggle_turtle(board[spider_pos])

    # Score
    score = 0
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(-119, -160)
    update_score()

    # Let's go
    counter = 0
    screen.update()
    game_loop()


def game_over():
    pen.goto(-80, -20)
    pen.color("white")
    pen.write("Game Over", font=("Arial", 24, "bold"))


def game_loop():
    global spider_pos, counter  # These values are modified within this function.
    toggle_turtle(board[spider_pos])
    spider_pos = random.randrange(NUM_ROWS * NUM_COLS)
    toggle_turtle(board[spider_pos])
    counter += 1
    if counter > NUM_TRIES:
        spider_pos = -999  # Avoid clicking in between rounds ??? memory
        game_over()
        canvas.after(2000, reset)
        return  # Very important to ensure loop is not called again.
    screen.ontimer(game_loop, SPEED)


if __name__ == "__main__":
    screen, canvas = init_screen()
    high_score = 0
    reset()
    turtle.done()