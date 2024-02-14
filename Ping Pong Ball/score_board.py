from turtle import Turtle
FONT=('courier',80,"normal")
class Score_board(Turtle):
    def __init__(self) :
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.write_score()
    
    def write_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(arg=self.left_score,align="center",font=(FONT))      # SCORE OF LEFT
        self.goto(100,200)
        self.write(arg=self.right_score,align="center",font=(FONT))     # SCORE OF RIGHT
    
    def increase_left(self):
        self.left_score+=1
        self.write_score()

    def increase_right(self):
        self.right_score+=1
        self.write_score()