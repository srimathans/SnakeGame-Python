from turtle import Turtle

class Highscore(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore = int(data.read())
        # self.highscore = 0
        self.create_high()

    def create_high(self):
        self.penup()
        self.hideturtle()
        self.color('red')
        self.setpos(70, 250)
        self.update_high(0)

    def update_high(self, score):
        if score > self.highscore:
            self.highscore = score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.highscore}")
            self.clear()
        self.write(f'High Score: {self.highscore}', font=("Arial", 18, "normal"))