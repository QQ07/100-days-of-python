from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score = {self.score}",
                   align="center", font=("Ariel", 24, "normal"))
        # self.write(self.score)

    def plus_one(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}",
                   align="center", font=("Ariel", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",
                   align="center", font=("Ariel", 24, "normal"))
