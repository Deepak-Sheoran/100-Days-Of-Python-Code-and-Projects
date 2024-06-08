from turtle import Turtle, Screen
from random import randint

field = Screen()
field.bgcolor("cyan")
field.title("Race Between Turtles")
painter = Turtle()
painter.pensize(2)
painter.speed("fastest")


def dashed_line(distance, obj=painter, step=20):
    starting_distance = 0
    while starting_distance <= distance:
        obj.forward(step)
        starting_distance += step
        if obj.isdown():
            obj.penup()
        else:
            obj.pendown()


painter.hideturtle()
painter.penup()
y_cor = -80
for i in range(6):
    painter.goto(-370, y_cor)
    painter.pendown()
    # painter.forward(740)
    dashed_line(740)
    painter.penup()
    y_cor += 40

painter.goto(-350, -90)
painter.left(90)
dashed_line(200)

painter.penup()
painter.goto(340, -90)
dashed_line(200)

racers = []
for i in range(5):
    new_racer = Turtle("turtle")
    racers.append(new_racer)

colors = ['red', 'blue', 'purple', 'orange', 'yellow']
index = 0
y_cor = -60
for racer in racers:
    racer.penup()
    racer.color(colors[index])
    index += 1
    racer.goto(-370, y_cor)
    y_cor += 40

guessed_winner = field.textinput("Time To Guess", "Enter the color of the turtle that you think will win _ ")


def race():
    while True:
        for r in racers:
            r.forward(randint(1, 10))
            if r.xcor() > 340:
                result = r.pencolor()
                print(f"The turtle with the {result} color wins the race")
                return result


actual_winner = race()
if actual_winner == guessed_winner:
    print("You were right!!")
else:
    print("You were wrong!!")

field.exitonclick()
