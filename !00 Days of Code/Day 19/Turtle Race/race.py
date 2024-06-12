from turtle import Turtle, Screen
from random import randint


def draw_dashed_line(distance, obj, step=20):
    starting_distance = 0
    while starting_distance <= distance:
        obj.forward(step)
        starting_distance += step
        if obj.isdown():
            obj.penup()
        else:
            obj.pendown()


class Race:

    def __init__(self, number_of_racers=5):
        self.racers = None
        self.who_won = None
        self.guessed_winner = None
        self.field = Screen()
        self.painter = Turtle()
        self.numbers = number_of_racers
        self.staring_initialization()
        self.create_track()
        self.create_racers()
        self.guess_winner()
        self.race()

    def staring_initialization(self):

        self.field.tracer(5)
        self.field.title("Race Between Turtles")
        self.field.bgpic("download.png")

        self.painter.hideturtle()
        self.painter.penup()
        self.painter.pensize(2)
        self.painter.speed("fastest")

    def create_track(self):
        y_cor = -80
        for i in range(6):
            self.painter.goto(-370, y_cor)
            self.painter.pendown()
            draw_dashed_line(740, self.painter)
            self.painter.penup()
            y_cor += 40

        self.painter.goto(-350, -90)
        self.painter.left(90)
        draw_dashed_line(200, self.painter)

        self.painter.penup()
        self.painter.goto(340, -90)
        draw_dashed_line(200, self.painter)
        self.field.tracer(1)

    def create_racers(self):
        self.racers = []
        for i in range(self.numbers):
            new_racer = Turtle("turtle")
            self.racers.append(new_racer)

        colors = ['red', 'blue', 'purple', 'orange', 'yellow']
        index = 0
        y_cor = -60
        for racer in self.racers:
            racer.penup()
            racer.color(colors[index])
            index += 1
            racer.goto(-370, y_cor)
            y_cor += 40

    def guess_winner(self):
        self.guessed_winner = self.field.textinput("Time To Guess", "Enter the color of the turtle that you"
                                                                    " think will win.")

    def race(self):
        while True:
            for r in self.racers:
                r.forward(randint(1, 10))
                if r.xcor() > 340:
                    self.who_won = r.pencolor()
                    print(f"The turtle with the {self.who_won} color wins the race")
                    self.field.exitonclick()
