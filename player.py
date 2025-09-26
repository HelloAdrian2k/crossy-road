from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.move_start_position()
        self.shape('turtle')
        self.setheading(90)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)
    
    def has_crossed(self):
        return self.ycor() >= FINISH_LINE_Y
    
    def move_start_position(self):
        self.goto(STARTING_POSITION)