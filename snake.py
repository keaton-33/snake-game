from turtle import Turtle
# Size scale for default value of 20 x 20
SIZE = (1, 1)
MOVE = 20
START_POS = [(10, -10), (-10, -10), (-30, 10)]


class Snake:
    def __init__(self):
        self.segments = []
        self.new_snake()
        self.head = self.segments[0]
        # self.head.color("gray")
        self.has_turned = False
        # self.new_direction = 0
        # self.turn_vertical = False
        # self.turn_horizontal = False

    def new_snake(self):
        """ Creates three segments at the x and y coordinates in the START_POS list """
        for i in START_POS:
            self.add_segment(i)

    def add_segment(self, position):
        """ Main mehtod for creating a new segment and appending it to the segments list """
        new_segment = Turtle("square")
        new_segment.speed(10)
        new_segment.penup()
        new_segment.color("white")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        """ Adds one new segment at the position of the last segment """
        self.add_segment(self.segments[-1].position())

    def move(self):
        """ Moves each segments position to the one in front of it, then moves the head forward by 20 units """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE)

    # def turn(self):
    #     if self.turn_vertical:
    #         while self.head.xcor() % 20 != 0:
    #             return
    #             # self.head.forward(MOVE)
    #         self.head.setheading(self.new_direction)
    #         self.turn_horizontal = False
    #     if self.turn_horizontal:
    #         while self.head.ycor() % 20 != 0:
    #             return
    #             # self.head.forward(MOVE)
    #         self.head.setheading(self.new_direction)
    #         self.turn_horizontal = False

        # if self.new_direction != self.head.heading():
        #     if self.new_direction == 90 or self.new_direction == 270:
        #         if self.head.xcor() % 20 == 0:
        #             self.head.setheading(self.new_direction)
        #     elif self.new_direction == 0 or self.new_direction == 180:
        #         if self.head.ycor() % 20 == 0:
        #             self.head.setheading(self.new_direction)


    def up(self):
        if self.head.heading() != 270 and not self.has_turned:
            # self.new_direction = 90
            # self.turn_vertical = True
            self.head.setheading(90)
            self.has_turned = True

    def down(self):
        if self.head.heading() != 90 and not self.has_turned:
            # self.new_direction = 270
            # self.turn_vertical = True
            self.head.setheading(270)
            self.has_turned = True

    def left(self):
        if self.head.heading() != 0 and not self.has_turned:
            # self.new_direction = 180
            # self.turn_horizontal = True
            self.head.setheading(180)
            self.has_turned = True

    def right(self):
        if self.head.heading() != 180 and not self.has_turned:
            # self.new_direction = 0
            # self.turn_horizontal = True
            self.head.setheading(0)
            self.has_turned = True

            # while xcor % 20 != 0: continue
            # Note to self: could also try putting the trigger into the main.py while loop
