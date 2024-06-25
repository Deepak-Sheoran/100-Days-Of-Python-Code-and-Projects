from turtle import Turtle

MOVE_DISTANCE = 20


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class Snake:
    def __init__(self, starting_length=3, color=None):

        part = Turtle("square")
        part.color(color)
        part.penup()
        self.head = Node(data=part)
        self.tail = None

        self.starting_length = starting_length
        # self.snake_body_parts = []
        # self.snake_create_body_parts()
        self.create_staring_body(color=color)

    # def snake_create_body_parts(self):
    #     for i in range(self.starting_length):
    #         body_part = Turtle("square")
    #         body_part.penup()
    #         body_part.color("white")
    #         body_part.back(i * 20)
    #         self.snake_body_parts.append(body_part)

    def create_staring_body(self, color=None):
        """
        1. Creates the snake body using the linked list
        """
        itr = self.head
        for i in range(1, self.starting_length + 1):
            part = Turtle("square")
            part.color(color)
            part.penup()
            part.goto(-i * 20, 0)
            itr.next = Node(part)
            itr = itr.next
        self.tail = itr

    def move(self):
        """
        2. Moves the snake, so it keeps moving in a particular direction
        """
        pos = self.head.data.pos()
        self.head.data.forward(MOVE_DISTANCE)
        itr = self.head.next
        while itr:
            pos1 = itr.data.pos()
            itr.data.goto(pos)
            pos = pos1
            itr = itr.next

    def add_node(self):
        itr = self.tail
        itr.next = Node(data=itr.data.clone())
        itr = itr.next
        itr.data.back(20)
        self.tail = itr

    def turn_left(self):
        if self.head.data.heading() != 0:
            self.head.data.setheading(180)

    def turn_right(self):
        if self.head.data.heading() != 180:
            self.head.data.setheading(0)

    def turn_up(self):
        if self.head.data.heading() != 270:
            self.head.data.setheading(90)

    def turn_down(self):
        if self.head.data.heading() != 90:
            self.head.data.setheading(270)

    def change_color(self, color):
        itr = self.head
        while itr:
            itr.data.color(color)
            itr = itr.next

    def detect_collision(self, obj=None):
        itr = self.head.next
        if obj is None:
            obj = self.head.data
        while itr:
            if obj.distance(itr.data) < 10:
                return True
            itr = itr.next
