from turtle import Turtle, Screen, colormode
from random import choice, randint

# colors = [
#     "#4B0082",  # Indigo
#     "#2F4F4F",  # Dark Slate Gray
#     "#696969",  # Dim Gray
#     "#708090",  # Slate Gray
#     "#778899",  # Light Slate Gray
#     "#2E8B57",  # Sea Green
#     "#556B2F",  # Dark Olive Green
#     "#8B4513",  # Saddle Brown
#     "#A0522D",  # Sienna
#     "#6B8E23",  # Olive Drab
#     "#808000",  # Olive
#     "#800000",  # Maroon
#     "#8B0000",  # Dark Red
#     "#483D8B",  # Dark Slate Blue
#     "#2B3856",  # Gunmetal
#     "#654321",  # Dark Brown
#     "#3C1414",  # Dark Scarlet
#     "#4F4F2F",  # Dark Olive
#     "#5F9EA0",  # Cadet Blue
#     "#3B3B3B",  # Charcoal
# ]

walker = Turtle()
space = Screen()
walker.shape("circle")
walker.shapesize(0.5, 0.5)
walker.pensize(15)
walker.speed("fastest")
colormode(255)
for _ in range(200):
    tup = (randint(0, 255), randint(0, 255), randint(0, 255))
    walker.color(tup)
    walker.forward(30)
    angle = choice([0, 90, 180, 270])
    walker.setheading(angle)
space.exitonclick()
