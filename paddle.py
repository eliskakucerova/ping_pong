from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto((self.position, 0))
        self.shapesize(stretch_wid=6, stretch_len=1, outline=None)
        self.showturtle()

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
