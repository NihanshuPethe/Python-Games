from turtle import Turtle

ALLIGMENT="center"
FONT=("Arial",12,"normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()   #Intake the turtle class 
        self.score=0
        self.hideturtle()
        self.up()
        self.goto(0,280)
        self.color("white")        
        self.print_score()

    def print_score(self):
        self.write(f"Score {self.score}",align=ALLIGMENT,font=FONT)
    
    def game_over(self):
        self.home()      # Print game over
        # self.goto(0,0)
        self.write(f"GAME OVER",align=ALLIGMENT,font=FONT)
        
    def score_increase(self):  # Print Current Score
        self.score+=1          #increament the score 
        self.clear()           # Clear the screen
        self.print_score()     #Print the current score
        
