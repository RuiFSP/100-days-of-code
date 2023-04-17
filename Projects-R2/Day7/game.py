import turtle
import random
import winsound

# Set up the screen
screen = turtle.Screen()
screen.register_shape("background.gif")
screen.setup(600, 600)
screen.bgcolor("black")
screen.bgpic("background.gif")
screen.title("Space Invaders")

# Create the player's spaceship
player = turtle.Turtle()
turtle.register_shape("player.gif")
player.shape("player.gif")
player.color("blue")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)
player_speed = 0

# Create the player's projectiles
projectiles = []

# Create the enemies
enemies = []
for i in range(5):
    enemy = turtle.Turtle()
    turtle.register_shape("invader.gif")
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.goto(-200 + i * 100, 250)
    enemy.speed = 2
    enemies.append(enemy)

# Create the enemy projectiles
enemy_projectiles = []

# Create scoring and game over
score = 0

score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

game_over = False

game_over_pen = turtle.Turtle()
game_over_pen.speed(0)
game_over_pen.color("white")
game_over_pen.penup()
game_over_pen.hideturtle()
game_over_pen.goto(0, 0)


# Define the player's movement functions
def move_left():
    global player_speed
    player_speed = -5


def move_right():
    global player_speed
    player_speed = 5


def stop():
    global player_speed
    player_speed = 0


def fire():
    global projectiles
    projectile = turtle.Turtle()
    projectile.color("yellow")
    projectile.shape("triangle")
    projectile.penup()
    projectile.speed(0)
    projectile.shapesize(0.5, 0.5)
    projectile.goto(player.xcor(), player.ycor() + 10)
    projectiles.append(projectile)
    projectile.showturtle()
    winsound.PlaySound("laser.wav", winsound.SND_ASYNC)


# Bind keyboard events to the player's movement functions
turtle.listen()
turtle.onkeypress(move_left, "Left")
turtle.onkeypress(move_right, "Right")
turtle.onkeyrelease(stop, "Left")
turtle.onkeyrelease(stop, "Right")
turtle.onkey(fire, "space")


# Define the explosion function
def explosion(x, y):
    explosion_turtle = turtle.Turtle()
    explosion_turtle.hideturtle()
    explosion_turtle.penup()
    explosion_turtle.goto(x, y)
    explosion_turtle.dot(80, "red")
    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
    for _ in range(15):
        explosion_turtle.shapesize(i * 0.5)
        explosion_turtle.stamp()
        explosion_turtle.shapesize((15 - i) * 0.5)
        explosion_turtle.stamp()
    explosion_turtle.clear()


# Modify the collision_detection function to add the explosion effect
def collision_detection():
    global score, game_over

    for enemy in enemies:
        for projectile in projectiles:
            if projectile.distance(enemy) < 20:
                winsound.PlaySound("laser.wav", winsound.SND_ASYNC)
                explosion(enemy.xcor(), enemy.ycor())
                enemy.goto(random.randint(-280, 280), random.randint(150, 250))
                score += 10
                score_pen.clear()
                score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
                projectile.hideturtle()
                projectiles.remove(projectile)

    for enemy_projectile in enemy_projectiles:
        if enemy_projectile.distance(player) < 20:
            player.hideturtle()
            enemy_projectile.hideturtle()
            explosion(player.xcor(), player.ycor())
            game_over_pen.write("Game Over!", align="center", font=("Courier", 24, "normal"))
            game_over = True
            break


# Define the enemy movement function
def move_enemy():
    global game_over
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy.speed
        enemy.setx(x)

        # Reverse direction and move down
        if enemy.xcor() > 280:
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemy.speed *= -1

        # Check for game over
        if enemy.ycor() < -250:
            game_over = True
            game_over_pen.write("GAME OVER", align="center", font=("Courier", 30, "normal"))
            break

        # Fire enemy projectiles
        if random.randint(1, 100) == 1:
            enemy_projectile = turtle.Turtle()
            enemy_projectile.color("white")
            enemy_projectile.shape("circle")
            enemy_projectile.penup()
            enemy_projectile.speed(0)
            enemy_projectile.shapesize(0.5, 0.5)
            enemy_projectile.goto(enemy.xcor(), enemy.ycor() - 20)
            enemy_projectiles.append(enemy_projectile)
            enemy_projectile.showturtle()


# Define the enemy projectile movement function
def move_enemy_projectile():
    for enemy_projectile in enemy_projectiles:
        y = enemy_projectile.ycor()
        y -= 5
        enemy_projectile.sety(y)

        # Check for collision with player
        if enemy_projectile.distance(player) < 20:
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            player.hideturtle()
            enemy_projectile.hideturtle()
            global game_over
            game_over = True
            game_over_pen.write("GAME OVER", align="center", font=("Courier", 30, "normal"))

        # Remove enemy projectile if it goes off-screen
        if enemy_projectile.ycor() < -300:
            enemy_projectile.hideturtle()
            enemy_projectiles.remove(enemy_projectile)


# Define the projectile movement function
def move_projectile():
    for projectile in projectiles:
        y = projectile.ycor()
        y += 10
        projectile.sety(y)

        # Remove projectile if it goes off screen
        if projectile.ycor() > 300:
            projectile.hideturtle()
            projectiles.remove(projectile)


# Main game loop
while not game_over:
    move_enemy()
    move_enemy_projectile()
    move_projectile()
    collision_detection()

    # Move player
    x = player.xcor()
    x += player_speed
    if x < -280:
        x = -280
    elif x > 280:
        x = 280
    player.setx(x)

# Keep the window open until the user closes it
turtle.done()
