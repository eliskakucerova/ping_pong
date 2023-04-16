from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dx = 10
        self.dy = 10
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce(self):
        self.dy *= -1

    def bounce_top(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() - 10
        self.goto(new_x, new_y)

    def bounce_bottom(self):
        new_x = self.xcor() - 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def reset(self):
        self.hideturtle()
        self.goto(x=0,y=0)
        self.showturtle()
        self.dx *= -1


