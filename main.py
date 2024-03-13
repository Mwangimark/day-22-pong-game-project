from turtle import Screen
from scoreboard import Scoreboard
from peddle import Peddle
from ball import Ball
import time
POS_L = (-350, 0)
POS_R = (350, 0)

peddle_l = Peddle(POS_L)
peddle_r = Peddle(POS_R)
ball = Ball()
screen = Screen()
scoreboard = Scoreboard()

# creating a screen
screen.title("Pong Game")
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)


screen.listen()
screen.onkey(peddle_r.move_up, "Up")
screen.onkey(peddle_r.move_down, "Down")
screen.onkey(peddle_l.move_up, "w")
screen.onkey(peddle_l.move_down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#     detect the hitting of wall
    if ball.ycor() > 280 or ball.ycor() < -280:
           ball.wall_bounce()

    if (ball.distance(peddle_r) < 50 and ball.xcor()>320) or (ball.distance(peddle_l)<50 and ball.xcor() <-320):
        ball.peddle_bounce()

    # peddle misses the ball
    if ball.xcor() > 390:
        scoreboard.l_point_score()
        ball.reset_game()

    if ball.xcor() < -390:
        scoreboard.r_point_score()
        ball.reset_game()

screen.exitonclick()
