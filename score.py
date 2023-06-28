from turtle import Turtle

FONT = ('Courier', 20, 'normal')

class Score (Turtle):

    def __init__(self):
        """counts the score"""
        super().__init__()
        self.points1 = 0
        self.points2 = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-300, 200)
        self.write(f"Player 1: {self.points1}", move=False, align="center", font=FONT)
        self.goto(300, 200)
        self.write(f"Player 2: {self.points2}", move=False, align="center", font=FONT)

    def set_end (self, player):
        """increases the score by one"""
        if player == 1:
            self.points1 += 1
        else:
            self.points2 += 1
        self.clear()
        self.goto(-300, 200)
        self.write(f"Player 1: {self.points1}", move=False, align="center", font=FONT)
        self.goto(300, 200)
        self.write(f"Player 2: {self.points2}", move=False, align="center", font=FONT)


    def game_over(self):
        """prints the winner once the game is over"""
        self.goto(0, 0)
        if self.points2 > self.points1:
            self.write("Player 2 WINS!!!", move=False, align="center", font=FONT)
        else:
            self.write("Player 1 WINS!!!", move=False, align="center", font=FONT)