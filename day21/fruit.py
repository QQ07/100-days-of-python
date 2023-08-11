from turtle import Turtle
import random

# position = (random.randint(1, 20)*20, random.randint(1, 20)*20)


# class Fruit:
#     def __init__(self) -> None:
#         self.createFruit()

#     def createFruit(self):
#         f = Turtle("square")
#         f.color("white")
#         f.penup()
#         f.goto(position)
#     def show(self):
        
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
    
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)
        