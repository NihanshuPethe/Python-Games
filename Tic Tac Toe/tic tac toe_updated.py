import os


def sum(a,b,c):
    return (a+b+c)    

def print_board(x_state,z_state):

    zero=  "X" if x_state[0] else("O" if z_state[0] else "9")
    one=   "X" if x_state[1] else("O" if z_state[1] else "1")
    two=   "X" if x_state[2] else("O" if z_state[2] else "2")
    three= "X" if x_state[3] else("O" if z_state[3] else "3")
    four=  "X" if x_state[4] else("O" if z_state[4] else "4")
    five=  "X" if x_state[5] else("O" if z_state[5] else "5")
    six=   "X" if x_state[6] else("O" if z_state[6] else "6")
    seven= "X" if x_state[7] else("O" if z_state[7] else "7")
    eight= "X" if x_state[8] else("O" if z_state[8] else "8")

    print(f" {seven} | {eight} | {zero} ")
    print("-----------")
    print(f" {four} | {five} | {six} ")
    print("-----------")
    print(f" {one} | {two} | {three} ")

def check_win(x_state,z_state):
    all_wins=[[7,8,0],[4,5,6],[1,2,3],[7,4,1],[8,5,2],[0,6,3],[7,5,3],[0,5,1]]
    for win in all_wins:
        if(sum(x_state[win[0]],x_state[win[1]],x_state[win[2]]) == 3):
            print_board(x_state,z_state)
            print("X Won the Game ")
            return 1
        if(sum(z_state[win[0]],z_state[win[1]],z_state[win[2]]) == 3):
            print_board(x_state,z_state)
            print("X Won the Game ")
            return 0
    return -1

if __name__=="__main__":
    print("Welcome to Tic Tac Toe Game ")
    # Game variable
    x_state=[0,0,0,0,0,0,0,0,0]
    z_state=[0,0,0,0,0,0,0,0,0]
    chance=1
    while(True):
        print_board(x_state,z_state)
        if chance==1:
            print("X chance")
            pos=int(input("Enter the Position "))
            pos=pos%9
            if z_state[pos]==1 or x_state[pos]==1 :
                print(f"{pos%9} is already occupied ")
                continue
            else:
                x_state[pos%9]=1

        elif chance==0:
            print("O chance")
            pos=int(input("Enter the Position "))
            pos=pos%9
            if x_state[pos%9]==1 or z_state[pos%9]==1:
                print(f"{pos%9} is already occupied ")
                continue
            else:
                z_state[pos%9]=1
        
        os.system('cls' if os.name == 'nt' else 'clear')   # cls if window (os.name== nt) else clear (linux)
        winner=check_win(x_state,z_state)
        
        if(winner != -1):       #break if winner is found
            break
        chance=1-chance
