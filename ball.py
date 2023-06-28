from turtle import Turtle
import random

MOVE_DISTANCE = 10


class Ball (Turtle):

    def __init__(self, left):
        """sets the ball for the game, if start player left, left = 1 if at player right left = -1"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("white")
        self.speed("fastest")
        self.reset_ball(left)


    def reset_ball (self, left):
        """resets the ball position after a set"""
        self.goto(-340 * left, 0)
        a = random.randint(0, 90)
        if left == -1:
            self.angle = a + 135
        elif a < 45:
            self.angle = 360 + (a - 45)
        else:
            self.angle = a - 45
        self.setheading(self.angle)


    def change_angel(self):
        """changes the angel if the ball hit the wall"""
        self.angle = 360 - self.angle
        self.setheading(self.angle)



    def hit_wall(self):
        """tests if ball hit the wall"""
        y = self.ycor()
        if y > 235 or y < -235:
            return True
        else:
            return False

    def move(self):
        """checks if the ball hit the wall and changes angel if needed than moves the ball """
        if self.hit_wall():
            self.change_angel()
        self.forward(MOVE_DISTANCE)



    def out_of_bounds (self):
        """checks if the ball is out of bounds"""
        x = self.xcor()
        if x > 385 or x < -385:
            return True
        else:
            return False


    def hit_player(self):
        """changes angel after the ball hits the paddle"""
        self.angle = 180 - self.angle
        if self.angle < 0:
            self.angle = 360 + self.angle
        self.setheading(self.angle)
        self.forward(20)


