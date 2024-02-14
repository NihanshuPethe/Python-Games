import turtle
from random import randint
colour_of_turtle=["red","orange","yellow","green","blue","purple"]
all_turtle=[]                                                 #Store all Turtle
screen=turtle.Screen()
win=turtle.Turtle()
win.hideturtle()
# Variable
FONT=('courier',24,"normal")
screen.setup(width=500,height=400)
is_game_on=False

user_player = screen.textinput(title="Select your turtle",prompt="Enter your choice from rainbow color")
while not user_player in colour_of_turtle:
    user_player = screen.textinput(title="Select your turtle",prompt="Enter your choice from rainbow color")

y=-135
for i in range(6):
    tim=turtle.Turtle()
    tim.up()
    tim.shape('turtle')
    tim.color(colour_of_turtle[i])
    tim.goto(-240,y)
    y+=50
    all_turtle.append(tim)
is_game_on=True
while is_game_on:
    for i in all_turtle:
        tim=i
        tim.forward(randint(1,10))
        current_loc=tim.xcor()
        if(current_loc>240):
            if(user_player==tim.color()):
                print(f"Winner is {tim.pencolor()} You win")
                screen.title(f"Winner is {tim.pencolor()} You win")
                win.write(f"Winner is {tim.pencolor()} ",align="center",font=FONT)
            else:
                print(f"Winner is {tim.pencolor()} You lose")
                screen.title(f"Winner is {tim.pencolor()} You win")
                win.write(f"Winner is {tim.pencolor()} ",align="center",font=FONT)
            is_game_on=False
            break    

screen.exitonclick()