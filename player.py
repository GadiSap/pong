from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_LEN = 5


class Player (Turtle):

    def __init__(self, x):
        """sets paddles"""
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=PADDLE_LEN)
        self.setheading(90)
        self.color("white")
        self.speed("fastest")
        self.goto(x, 0)


    def reset_player (self, x):
        self.goto(x, 0)


    #sets the move up and down functions
    def up (self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
        if -205 >= self.ycor() or self.ycor() >= 205:
            self.backward(MOVE_DISTANCE)

    def down (self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)
        if -205 >= self.ycor() or self.ycor() >= 205:
            self.backward(MOVE_DISTANCE)




