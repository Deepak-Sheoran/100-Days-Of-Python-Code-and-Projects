from turtle import Turtle, Screen, colormode
from random import choice
import colorgram

canvas = Screen()
canvas.title("Damien Hirst Painting")
painter = Turtle()
print(painter.pos())
painter.shape("circle")
painter.pensize(20)
painter.speed("fastest")
colormode(255)

colors = colorgram.extract("spot painting.jpeg", 20)


for i in range(-300, 320, 50):
    for j in range(-360, 390, 50):
        painter.penup()
        painter.goto(j, i)
        painter.color(choice(colors).rgb)
        painter.stamp()
        painter.pendown()
canvas.exitonclick()
