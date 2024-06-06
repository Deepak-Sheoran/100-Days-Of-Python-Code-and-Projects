from turtle import Turtle, Screen
from random import choice

canvas = Screen()
canvas.title("Damien Hirst Painting")
painter = Turtle()
print(painter.pos())
painter.shape("circle")
painter.shapesize(0.5, 0.5, 0.5)
painter.speed(10)

colors = [
    "#FFB6C1",  # Light Pink
    "#FFCCCB",  # Misty Rose
    "#FFDAB9",  # Peach Puff
    "#E6E6FA",  # Lavender
    "#FFFACD",  # Lemon Chiffon
    "#E0FFFF",  # Light Cyan
    "#F0FFF0",  # Honeydew
    "#FAFAD2",  # Light Goldenrod Yellow
    "#FFEFD5",  # Papaya Whip
    "#FFF5EE",  # Seashell
    "#F5F5DC",  # Beige
    "#F5DEB3",  # Wheat
    "#F0E68C",  # Khaki
    "#EEDD82",  # Light Goldenrod
    "#D8BFD8",  # Thistle
    "#D3D3D3",  # Light Gray
    "#B0E0E6",  # Powder Blue
    "#ADD8E6",  # Light Blue
    "#E0FFFF",  # Light Cyan
    "#98FB98"   # Pale Green
]


for i in range(-300, 320, 20):
    for j in range(-370, 390, 20):
        painter.penup()
        painter.goto(j, i)
        painter.color(choice(colors))
        painter.stamp()
        painter.pendown()
canvas.exitonclick()
