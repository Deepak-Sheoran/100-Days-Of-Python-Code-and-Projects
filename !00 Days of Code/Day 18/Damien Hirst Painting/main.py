from turtle import Turtle, Screen, colormode
from random import choice
import colorgram

canvas = Screen()
canvas.title("Damien Hirst Painting")
painter = Turtle()
print(painter.pos())
painter.speed("fastest")
painter.hideturtle()
colormode(255)
painter.penup()

colors = colorgram.extract("spot painting.jpeg", 20)


for i in range(-300, 350, 50):
    painter.goto(-350, i)
    for j in range(1, 16):
        painter.dot(20, choice(colors).rgb)
        painter.forward(50)
canvas.exitonclick()
