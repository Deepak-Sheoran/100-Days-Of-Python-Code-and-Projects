from turtle import Turtle
from random import randint, choice


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speed("fastest")
        self.screen_color = None
        self.c = None

    def change(self, color=None, screen_color=None):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
        self.color(color)
        self.c = color
        self.screen_color = screen_color
        return x, y
