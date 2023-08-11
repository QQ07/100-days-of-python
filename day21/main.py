'''Snake Game🐍'''

from turtle import Screen
import time
from snake import Snake
from fruit import Food
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True

fruit = Food()
score = Score()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # fruit.show()
    scoree = 1
    if snake.head.distance(fruit) < 15:
        fruit.refresh()
        score.plus_one()
        snake.extend()
        # score.write(scoree, move=False, align='left', font=('Arial', 8, 'normal'))

    # detect collision with wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280):
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()
