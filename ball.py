from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("skyblue")
        self.shape("circle")
        self.penup()
        self.x_move = 4
        self.y_move = 4
        self.move_speed = 0.03

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def wall_collision(self):
        self.y_move *= -1

    def x_collision(self):
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        self.goto(0, 0)
        self.x_collision()
        self.move_speed = 0.03
