'''Snake Game🐍'''

from turtle import Screen, Turtle

def screen_setup():
    '''Set up Everything related to the screen and returns the screen object'''
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    return screen

def draw_snake(size_of_snake):
    '''Draws the snake with head at given coordinates and it's size'''
    for i in range(size_of_snake):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("white")
        tim.goto(x=0-20*i, y=0)

def main():
    '''Does it all'''
    screen = screen_setup()
    draw_snake(3)

    screen.exitonclick()

main()
 