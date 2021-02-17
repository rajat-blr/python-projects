#!/usr/bin/env python3

theboard = {'7': ' ','8': ' ','9':' ',
         '4': ' ','5': ' ','6':' ',
         '1': ' ','2': ' ','3':' '}

board_keys = []

for key in theboard:
    board_keys.append(key)

"""The following function prints the corresponding key value of the number in the above defined dictionary"""
def printboard(board):
    print(board['7']  + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4']  + '|' + board['5'] + '|' +  board['6'])
    print('-+-+-')
    print(board['1']  + '|' + board['2'] + '|' +  board['3'])


def game():
    turn = 'X'
    count = 0


    for i in range(10):
        printboard(theboard)
        print(turn + "Move to which place?")

        move = input()

        if theboard[move] == ' ':
            theboard[move] = turn
            count+=1
        else:
            print("Place is already filled,choose another place")
            continue

        '''check the winner after every 5 moves'''
        if count>=5:
            if theboard['7']==theboard['8']==theboard['9']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")
                break
            elif theboard['4']==theboard['5']==theboard['6']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")    
                break
            elif theboard['1']==theboard['2']==theboard['3']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")
                break
            elif theboard['1']==theboard['4']==theboard['7']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")    
                break
            elif theboard['2']==theboard['5']==theboard['8']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")
                break    
            elif theboard['3']==theboard['6']==theboard['9']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")
                break    
            elif theboard['1']==theboard['5']==theboard['9']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")
                break    
            elif theboard['3']==theboard['5']==theboard['7']!=' ':
                print(theboard)
                print("Game Over\n") 
                print(turn + "WON")    
                break

        if count == 9:
            print("\nGame Over\n")
            print("Its a tie!!")

        '''Now we need to change the turn of the player after every move'''

        if turn == 'X':
            turn = '0'

        else:
            turn = 'X'

    
    restart = input("Do you wanna play again?(y/n)")
    if restart =='y' or restart=='Y':
        for key in board_keys:
            theboard[key] = " "
        game()    


if __name__ == "__main__":
    game()