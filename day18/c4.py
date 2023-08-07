'''Random walk'''

import turtle as t
import random as R

timmy = t.Turtle()

colours = ["cyan", "dark slate gray", "blue", "green", "red",
           "spring green", "orange red", "purple", "violet", "thistle"]
timmy.speed("fastest")
timmy.width(3)
for _ in range(500):
    timmy.color(R.choice(colours))
    angle = R.choice([0,90,180,270])
    timmy.right(angle)
    timmy.forward(20)


screen = t.Screen()
screen.exitonclick()
