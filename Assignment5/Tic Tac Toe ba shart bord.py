import random
import time

def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j], end=" ")
        print() 


def check():  #barande shodan

    for i in range (0, 3):
        if game[i][0] == game [i][1] == game [i][2] == "x":
            print("player1 wins") 
            exit() 

        if game[i][0] == game [i][1] == game [i][2] == "o":
            print("player2 wins") 
            exit()

    

    for j in range (0, 3):
        if game[0][j] == game [1][j] == game [2][j] == "x":
            print("player1 wins") 
            exit() 

        if game[0][j] == game [1][j] == game [2][j] == "o":
            print("player2 wins") 
            exit()       


    if game [0][0] == game [1][1] == game [2][2] == "x":
        print("player1 wins") 
        exit() 

    if game [0][0] == game [1][1] == game [2][2] == "o":
        print("player2 wins") 
        exit() 

    if game [0][2] == game [1][1] == game [2][0] == "x":
        print("player1 wins") 
        exit() 

    if game [0][2] == game [1][1] == game [2][0] == "o":
        print("player2 wins") 
        exit() 



game = [["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]

show_game_board()  #satro sotoon bazi ro khali chap kon

while True:
    print("player1")
    while True:
        row = int(input("satr ra vared kon:")) 
        col = int(input("sotoon ra vared kon:"))   #shomare satro sotoono az bazikon begir
        if 0 <= row <= 2 and 0 <= col <= 2: #aya adad dar range hast?
            if game[row][col] == "_": #aya khoone khalie?
                game[row][col] = "x" # mohre x dar safheye bazi gharar bede
                break
            else:
                print("cell is not empty!")
        else:
            print("index out of range, try again")

    show_game_board()  #satro sotoon bazi ro ba vojjode mohre x chap kon
    check()

    print("player2")
    while True:
        row = int(input("satr ra vared kon:")) 
        col = int(input("sotoon ra vared kon:"))
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game[row][col] == "_":
                game[row][col] = "o" # mohre x dar safheye bazi gharar bede
                break
            else:
                print("cell is not empty!")
        else:
            print("index out of range, try again")
    
    show_game_board()  
    check()  
