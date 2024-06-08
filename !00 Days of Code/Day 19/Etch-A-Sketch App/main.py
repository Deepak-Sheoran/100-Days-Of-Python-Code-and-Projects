from turtle import Turtle, Screen

pen = Turtle()
canvas = Screen()


def forward(steps=10):
    pen.forward(steps)


def backward(steps=10):
    pen.back(steps)


def tilt_left():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)


def tilt_right():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)


def clear():
    canvas.resetscreen()


canvas.listen()
# The method .onkey is like a high order function because its taking another function as an argument.
canvas.onkey(forward, "w")
canvas.onkey(backward, "s")
canvas.onkey(tilt_right, "d")
canvas.onkey(tilt_left, "a")
canvas.onkey(pen.penup, "Up")
canvas.onkey(pen.pendown, "Down")
canvas.onkey(clear, "c")

canvas.exitonclick()
