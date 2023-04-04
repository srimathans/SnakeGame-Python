from turtle import Turtle

class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('red')

    def declare(self):
        self.write("Game Over", align="center", font=('Arial', 20, 'normal'))