import turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from gameover import Gameover
from highscore import Highscore

my_screen = Screen()
my_screen.setup(600, 600)
my_screen.bgcolor('black')
my_screen.title('my snake game')
my_screen.tracer(0)

my_snake = Snake()
my_gameover = Gameover()
my_food = Food()
my_scoreboard = Scoreboard()
my_highscore = Highscore()

my_screen.listen()
my_screen.onkey(my_snake.up, 'Up')
my_screen.onkey(my_snake.down, 'Down')
my_screen.onkey(my_snake.right, 'Right')
my_screen.onkey(my_snake.left, 'Left')


def game_on():
    my_screen.update()
    time.sleep(0.2)
    my_snake.move()

    dis = my_snake.objects[0].distance(my_food)
    if dis < 15:
        my_food.refresh()
        my_scoreboard.change_score()
        my_snake.add_length()

    wall_x = my_snake.objects[0].xcor()
    wall_y = my_snake.objects[0].ycor()

    if wall_x < -290 or wall_x > 290 or wall_y < -290 or wall_y > 290:
        my_highscore.update_high(my_scoreboard.score)
        my_gameover.declare()
        print('declare')
        return

    for i in range(1, len(my_snake.objects)):
        if my_snake.objects[0].distance(my_snake.objects[i]) < 5:
            my_highscore.update_high(my_scoreboard.score)
            my_gameover.declare()
            return
    game_on()

game_on()

def restart():
    my_gameover.clear()
    my_scoreboard.score_reset()
    my_snake.snake_reset()
    game_on()

my_screen.onkey(restart, 'r')













turtle.done()