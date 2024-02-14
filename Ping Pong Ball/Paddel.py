from turtle import Turtle

class paddel(Turtle):               #create a paddel for that 
    def __init__(self,position) :
        super().__init__()
        self.shape("square")                                # Square is of pixal 20x20 
        self.shapesize(stretch_len=1,stretch_wid=5)         # Turtle is of len 20pix & wid 100 pix because 20x5=100
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y=self.ycor()+30
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-30
        self.goto(self.xcor(),new_y)
