import random

choices = [1, 2, 3]
scores = {'player':0, 'computer':0} 

for i in range(10):
    computer_choice = random.choice(choices)
    print("Rock Paper Scissor Game")
    print("1 for Rock","2 for Paper","3 for Scissor",end="\n")
    player_choice = int(input('Player please choose your option:'))

    if((player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 3) or (player_choice == 3 and computer_choice == 1)): 
        print('computer wins')
        scores['computer'] += 1
    elif((player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2)):
        print('player wins')
        scores['player'] += 1

    if scores['player']> scores['computer']:
                print("Congratulations player wins")
                print("Score is:",scores['player'],"Computer score:",scores['computer'],end=" ")
    elif scores['computer']> scores['player']:
                print("Computer wins")
                print("Score is:",scores['player'],"Computer score:",scores['computer'],end=" ")
    else:
                print("Both win")
                

    user_choice=input('Do you want to continue? (y/n)')
    if user_choice =='y':
        continue             
    else:
        break  