from turtle import Turtle, Screen

ground = Screen()
runner = Turtle()

for _ in range(35):
    runner.forward(10)
    if runner.isdown():  # checks to see if the pen is down or not, if the pen is down then we make it up and vice versa
        # which gives us the dashed line in turn.
        runner.penup()
    else:
        runner.pendown()

ground.exitonclick()
