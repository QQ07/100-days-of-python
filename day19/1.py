'''etch a sketch'''
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    '''tim will move forward 10 spaces'''
    tim.forward(10)


def move_backward():
    '''tim will move backward 10 spaces'''
    tim.backward(10)


def rotate_clock():
    '''tim will rotate ACW'''
    tim.right(4)


def Rotate_anti_clock():
    '''tim will rotate ACW'''
    tim.left(4)


def clear_screen():
    '''screen will be cleared'''
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=Rotate_anti_clock)
screen.onkey(key="d", fun=rotate_clock)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
