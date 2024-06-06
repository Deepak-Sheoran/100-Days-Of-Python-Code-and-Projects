from turtle import Turtle, Screen
from random import choice

painter = Turtle()
canvas = Screen()
colors = ["red", "yellow", "blue", "green", "violet", "black", "grey"]

for no_of_sides in range(3, 10):
    painter.color(choice(colors))
    for _ in range(no_of_sides):
        painter.forward(100)
        angle = 360 / no_of_sides
        painter.right(angle)

canvas.exitonclick()
