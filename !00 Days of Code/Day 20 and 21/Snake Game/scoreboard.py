from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
