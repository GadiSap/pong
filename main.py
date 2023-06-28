from turtle import Screen
import time
from ball import Ball
from player import Player
from score import Score

BALLSPEED = 0.035
WINNING_POINTS = 5
X_LOC1 = -360
X_LOC2 = 360

screen = Screen()
# screen.clear()
screen.title("Ping Pong")
screen.setup(width = 800, height=500)
screen.bgcolor("black")
screen.tracer(0)


#set playes, score and ball objects
player_set = -1 # sets the starting player and later is updated to the last player to touch the ball
ball = Ball(player_set)
player1 = Player(-360)
player2 = Player(360)
score = Score()

screen.update()
#sets screen listen method to follow user input
screen.listen()
screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")
screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

#Run game
game_on = True
while game_on:
    set_on = True
    while set_on:
        ball.move()
        screen.update()
        time.sleep(BALLSPEED)
        #checks if ball hits the player's paddle
        if ball.distance(player1) < 50 and 0 < -X_LOC1  + ball.xcor() < 20:
            player_set = 1
            ball.hit_player()
            screen.update()
        elif ball.distance(player2) < 50 and 0 < X_LOC2 - ball.xcor() < 20:
            player_set = -1
            ball.hit_player()
            screen.update()
        #If ball out of bounds ends the set and gives points
        if ball.out_of_bounds():
            set_on = False
            score.set_end (player_set)
            player1.reset_player(X_LOC1)
            player2.reset_player(X_LOC2)
            ball.reset_ball(player_set)
    #test to see if one of the players won the game. If true ends the game.
    if score.points1 == WINNING_POINTS or score.points2 == WINNING_POINTS:
        score.game_over()
        game_on = False






screen.exitonclick()
