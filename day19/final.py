'''Turtle Racing Game'''
from turtle import Turtle, Screen
import random as R
screen = Screen()
screen.setup(width=600, height=400)
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

all_turtles = []

for i in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x=-270, y=-150+i*50)
    all_turtles.append(tim)


user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a colour")

race_on = True

while race_on:
    for turtle in all_turtles:
        turtle.forward(R.randint(0, 10))
        if turtle.xcor() > 270:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("SAAT KAROD!")
            else:
                print("abey padhai likhai pe dhyan do! ye jua band karo!")

screen.exitonclick()
