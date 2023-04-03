import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Create the bricks
bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for y in range(5):
    for x in range(-6, 7):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[y])
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(x * 70, 250 - y * 30)
        bricks.append(brick)

# Create the score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.penup()
score_pen.goto(-280, 360)
score_pen.write("Score: {}".format(score), align="left", font=("Courier", 24, "normal"))


# Define the paddle movement
def move_left():
    x = paddle.xcor()
    x -= 20
    if x < -280:
        x = -280
    paddle.setx(x)


def move_right():
    x = paddle.xcor()
    x += 20
    if x > 280:
        x = 280
    paddle.setx(x)


# Bind the paddle movement to the keyboard
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game loop
while True:

    try:
        time.sleep(0.02)
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Check for wall collisions
        if ball.xcor() > 290:
            ball.setx(290)
            ball.dx *= -1
        if ball.xcor() < -290:
            ball.setx(-290)
            ball.dx *= -1
        if ball.ycor() > 390:
            ball.goto(0, 0)
            ball.dy *= -1
            score -= 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="left", font=("Courier", 24, "normal"))
            time.sleep(1)
        if ball.ycor() < -390:
            break

        # Check for paddle collision
        if (ball.ycor() < -340) and (ball.ycor() > -350) and (ball.xcor() > paddle.xcor() - 50) and (
                ball.xcor() < paddle.xcor() + 50):
            ball.dy *= -1

        # Check for brick collisions
        for brick in bricks:
            if ball.distance(brick) < 40:
                brick.goto(1000, 1000)
                bricks.remove(brick)
                ball.dy *= -1
                score += 10
                score_pen.clear()
                score_pen.write("Score: {}".format(score), align="left", font=("Courier", 24, "normal"))

        # Check for win condition
        if len(bricks) == 0:
            score_pen.goto(0, 0)
            score_pen.write("You Win!", align="center", font=("Courier", 48, "normal"))
            break

        # Check for game over
        if ball.ycor() < -390:
            score_pen.goto(0, 0)
            score_pen.write("Game Over", align="center", font=("Courier", 48, "normal"))
            break

    except turtle.Terminator:
        break

screen.exitonclick()
