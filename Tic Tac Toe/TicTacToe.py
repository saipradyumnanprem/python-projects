'''

created on:
@author: saipradyumnanprem

'''

board = {
            '7':'' , '8':'', '9':'',
            '4':'' , '5':'', '6':'',
            '1':'' , '2':'', '3':''
        }

boardkey=[]

for key in board:
    boardkey.append(key)

def printBoard(board):
    print(board['7'] +'  |  ' + board['8'] + '  |  ' + board['9'])
    print('-- + -- + --')
    print(board['4'] +'  |  ' + board['5'] + '  |  ' + board['6'])
    print('-- + -- + --')
    print(board['1'] +'  |  ' + board['2'] + '  |  ' + board['3'])


#printBoard(board)

def game():
    turn = 'X'
    count = 0

    for i in range(10):

        printBoard(board)
        print("It is turn of " + turn + ". Specify the place you want it to be at: ")
        move = input()

        if board[move] == '':
            board[move] = turn
            count += 1
        else:
            print("This cell location is filled. Please choose another one.")
            continue

        if count >= 5:
            if board['7'] == board['8'] ==  board['9'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['4'] == board['5'] ==  board['6'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['1'] == board['2'] ==  board['3'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['7'] == board['4'] ==  board['1'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['8'] == board['5'] ==  board['2'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['9'] == board['6'] ==  board['3'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['7'] == board['5'] ==  board['3'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

            if board['1'] == board['5'] ==  board['9'] != ' ':
                printBoard(board)
                print("Game Over!")
                print("Player {} wins the game!".format(turn))
                break

        if count == 9:
            print("Game Over!")
            print("The game is tied!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to restart the game? (y/n) ")

    if restart == 'y' or restart == 'Y':
        for key in boardkey:
            board[key] = ' '
        game()



if __name__ == "__main__":
    game()