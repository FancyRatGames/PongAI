import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

BALL_RADIUS = 20
PAD_HEIGHT = 100
PAD_WIDTH = 10

# Create the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.shapesize(BALL_RADIUS/10)
ball.penup()

# Create the paddles
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(PAD_HEIGHT/10, PAD_WIDTH/10)
paddle1.penup()
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(PAD_HEIGHT/10, PAD_WIDTH/10)
paddle2.penup()

# Set the ball's initial position and velocity
ball.goto(0, 0)
ball_vel = [random.uniform(2, 5), random.uniform(-5, 5)]

# Set the paddles' initial positions
paddle1.goto(-375, 0)
paddle2.goto(375, 0)

# Move the ball
def move_ball():
    ball.setx(ball.xcor() + ball_vel[0])
    ball.sety(ball.ycor() + ball_vel[1])

    # Check if the ball hits the walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball_vel[1] *= -1
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball_vel[0] *= -1

    # Check if the ball hits the paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball_vel[0] *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball_vel[0] *= -1
    wn.ontimer(move_ball, 10)

# Move the paddles
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20

wn.listen()
wn.onkeypress(paddle1_up, "Up")
wn.onkeypress(paddle1_down, "Down")
wn.onkeypress(paddle2_up, "w")
wn.onkeypress(paddle2_down, "s")

move_ball()   
wn.mainloop()
