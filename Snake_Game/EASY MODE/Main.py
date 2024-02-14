import turtle  #Import turtle module
import time    #Import Time module

from snake import Snake                 # Import the 3 different files 
from food import Food                   # Import the 3 different files 
from scorebord import Scoreboard        # Import the 3 different files 

screen=turtle.Screen()           #  this line on code specify how the screen of the snake game shoule 
screen.bgcolor("black")          #  be like(black background , 600X600 display,title of screen ) etc
screen.setup(600,600)            #  
screen.title("My snake game ")   #
screen.tracer(0)  #IMP           # This is very important because of Tracer we are able to see snake which is made of 3 object as one object 

snake_object=Snake()               #snake object
food_object=Food()                 #food object
scoreboard_object=Scoreboard()     #scoreboard object

screen.listen()                             # Listen to the user input for live play
screen.onkey(snake_object.up,"Up")                 # UP arrow
screen.onkey(snake_object.down,"Down")             # DOWN arrow
screen.onkey(snake_object.left,"Left")             #LEFT arrow
screen.onkey(snake_object.right,"Right")           #RIGHT arrow

is_game_start=True

while is_game_start: #Here the game start
    screen.update()  #update the img ones the snake is moved
    time.sleep(0.1)  
    #If snake hit hte food then change the food location and extend the snake body and increase the score
    if(snake_object.head.distance(food_object)<15):
        food_object.refresh()  #Change the food location
        snake_object.extend()  #Increase the body of the snake 
        scoreboard_object.score_increase()  # Increase the score of the user
    
    snake_object.move()
    if(snake_object.head.xcor()>280):
        snake_object.left_side(snake_object.head.ycor())
    elif(snake_object.head.xcor()< -280):
        snake_object.right_side(snake_object.head.ycor())
    elif(snake_object.head.ycor()>280):
        snake_object.down_side(snake_object.head.xcor())
    elif(snake_object.head.ycor()< -280):
        snake_object.up_side(snake_object.head.xcor())
    #If Snake Hit itself
    for item in snake_object.segment[1:]:
        if(snake_object.head.distance(item)<10):
            is_game_start=False
            scoreboard_object.game_over()

screen.exitonclick() 