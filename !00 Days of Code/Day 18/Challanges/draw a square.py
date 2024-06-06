from turtle import Turtle, Screen

canvas = Screen()
runner = Turtle()

runner.pendown()
for i in range(4):
    runner.forward(100)
    runner.left(90)

canvas.exitonclick()
