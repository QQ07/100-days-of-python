'''Making different shapes'''

from turtle import Turtle, Screen
import random as R
timmy = Turtle()

colours = ["cyan", "dark slate gray", "blue", "green", "red",
           "spring green", "orange red", "purple", "violet", "thistle"]
for i in range(3, 100):

    timmy.color(R.choice(colours))
    angle = 360/i
    timmy.forward(30)
    for j in range(i-1):
        timmy.right(angle)
        timmy.forward(30)
    timmy.right(angle)

screen = Screen()
screen.exitonclick()
