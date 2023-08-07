'''Exploring Turtle in python'''

from turtle import Turtle, Screen
import random
timmy = Turtle()
# timmy.shape('turtle')
# timmy.color('Cyan')

# for i in range(100):
#     timmy.forward(random.randint(1, 10))
#     timmy.left(random.randint(1, 180))

for i in range(100):
    print(i)
    if (i % 2 == 0):
        timmy.penup()
        timmy.forward(10)
    else:
        # timmy.setx(20)
        timmy.pendown()
        # timmy.color("black")
        timmy.forward(10)


screen = Screen()
screen.exitonclick()
