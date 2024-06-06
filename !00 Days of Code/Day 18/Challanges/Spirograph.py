from turtle import Turtle, Screen, colormode
from random import randint

pen = Turtle()
page = Screen()
pen.speed("fastest")
colormode(255)

for i in range(0, 360, 5):
    pen.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    pen.setheading(i)
    pen.circle(100)

page.exitonclick()
