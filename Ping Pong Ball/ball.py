from turtle import Turtle

class Ball(Turtle):                 #Create a ball 
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ballspeed=0.1
        self.x=10
        self.y=10

    def move(self):                  # ball moves by increasing there x and y cor
        new_xcor= self.xcor()+self.x
        new_ycor=self.ycor()+self.y
        self.goto(new_xcor,new_ycor)

    def change_ycor(self):
        self.y*=-1
    def change_xcor(self):           #this function is called when the ball hit the paddel
        self.x*=-1
        self.ballspeed*=0.9