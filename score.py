from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("skyblue")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-50, 220)
        self.write(self.l_score, align="center", font=("Helvetica", 40, "normal"))
        self.goto(50, 220)
        self.write(self.r_score, align="center", font=("Helvetica", 40, "normal"))
        self.goto(0, 223)
        self.write(":", align="center", font=("Helvetica", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
