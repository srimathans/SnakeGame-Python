from turtle import Turtle, Screen
from food import Food
COORD = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    def __init__(self):
        self.objects = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.objects.append(Turtle('square'))
            self.objects[i].color('white')
            self.objects[i].penup()
            self.objects[i].setpos(COORD[i])

    def add_length(self):
        self.objects.append(Turtle('square'))
        new_len = len(self.objects) - 1
        self.objects[new_len].color('white')
        self.objects[new_len].penup()
        self.objects[new_len].setpos(self.objects[new_len - 1].xcor(), self.objects[new_len - 1].ycor())


    def move(self):
        for i in range(len(self.objects)-1, 0, -1):
            self.objects[i].goto(self.objects[i - 1].xcor(), self.objects[i - 1].ycor())
        self.objects[0].forward(20)

    def up(self):
        if self.objects[0].heading() != DOWN:
            self.objects[0].setheading(UP)

    def down(self):
        if self.objects[0].heading() != UP:
            self.objects[0].setheading(DOWN)

    def left(self):
        if self.objects[0].heading() != RIGHT:
            self.objects[0].setheading(LEFT)

    def right(self):
        if self.objects[0].heading() != LEFT:
            self.objects[0].setheading(RIGHT)

    def snake_reset(self):
        for part in self.objects:
            part.goto(1000, 1000)
        self.objects.clear()
        self.create_snake()



