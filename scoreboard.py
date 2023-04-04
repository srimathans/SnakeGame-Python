from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.create_score_turtle()

    def create_score_turtle(self):
        self.penup()
        self.hideturtle()
        self.shape('triangle')
        self.color('red')
        self.setpos(-200, 250)
        self.change_score()


    def change_score(self):
        self.score+=1
        self.clear()
        self.write(f'score: {self.score}', font=('Arial', 18, 'normal'))

    def score_reset(self):
        self.score = -1
        self.change_score()







