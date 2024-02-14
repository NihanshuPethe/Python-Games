from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) :
        super().__init__()  #constructor of turtle object is called
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()
    
    def refresh(self):        # generate the food at random place
        new_x=randint(-280,280)
        new_y=randint(-280,280)
        self.goto(new_x,new_y)