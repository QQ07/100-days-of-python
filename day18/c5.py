'''Random walk'''

import turtle as t
import random as R

timmy = t.Turtle()

colours = ["cyan", "dark slate gray", "blue", "green", "red",
           "spring green", "orange red", "purple", "violet", "thistle"]
timmy.speed("fastest")
# timmy.width(3)
for i in range(36):
    timmy.color(R.choice(colours))
    timmy.circle(50)
    timmy.setheading(timmy.heading()+10)
    

screen = t.Screen()
screen.exitonclick()
