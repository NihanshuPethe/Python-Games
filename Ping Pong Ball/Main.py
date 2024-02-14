import turtle
from Paddel import paddel
import time
from ball import Ball
from score_board import Score_board

# For Screen
screen=turtle.Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)
screen.title("Pong")
#All OBJECT
left_player=paddel((-360,0))   #left paddel
right_player=paddel((360,0))   #right paddel
ball=Ball()                    #ball 
score_board=Score_board()      #Score Table
# interact with game

screen.update()
screen.listen()
screen.onkey(left_player.go_up,"w")
screen.onkey(left_player.go_down,"s")
screen.onkey(right_player.go_up,"Up")
screen.onkey(right_player.go_down,"Down")

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(ball.ballspeed)
    # hit wall
    if (ball.ycor()>280 or ball.ycor()<-280 ):    # if ball hit the upper and the lower ball just change the y co-ordinate
        ball.change_ycor()
    
    # hit paddel
    if(ball.distance(right_player)<50 and ball.xcor()>330 or ball.distance(left_player)<50 and ball.xcor()< -330):
        ball.change_xcor()       #if ball hit the paddel just change the x axis and increase the speed


    # if left player miss
    if(ball.xcor()>380): # means ball touch the left wall just change the reset the ball loc and increase the score of right player
        ball.home()
        ball.change_xcor()
        score_board.increase_right()
        ball.ballspeed=0.1
    # if right player miss
    elif(ball.xcor()<-380):      
        ball.home()    
        ball.change_xcor()
        score_board.increase_left()
        ball.ballspeed=0.1
    ball.move()

screen.exitonclick()