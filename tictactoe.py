#This function displays TicTacToe Board
def display_board(test_board):
    print('_____________')
    # print('|   |   |   |')
    print('| '+test_board[1]+' |'+' '+test_board[2]+' '+'| '+test_board[3]+' |')
    # print('|   |   |   |')
    print('-------------')
    # print('|   |   |   |')
    print('| '+test_board[4]+' '+'| '+test_board[5]+' '+'| '+test_board[6]+' |')
    # print('|   |   |   |')
    print('-------------')
    # print('|   |   |   |')
    print('| '+test_board[7]+' '+'| '+test_board[8]+' '+'| '+test_board[9]+' |')
    # print('|   |   |   |')
    print('-------------')

#This function Asks players to choose between X and O marks
def player_input():
    while True:
        Input = input('Enter your choice X or O')
        if(Input.lower() == 'x' or Input.lower() == 'o'):
            break
        else:
            print('Enter correct option from X or O')
            continue
    if Input.upper() == 'X':
        return 'X'

#This Function Chooses who play First
import random
def choose_first():
    if(random.randint(0,1) == 1):
        return 'Player1'
    else:
        return 'Player2'

#This function MArks Place with Sign X or O
def place_marker(board, marker, position):
    board[position] = marker

#This function CHecks whether anyone wins
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark))
    pass

#This function checks whther position is empty or already filled
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for space in range(1,10):
        if space_check(board,space):
            return False
    return True

def player_choice(board):
    place = 0

    while(place not in [1,2,3,4,5,6,7,8,9] or not space_check(board,place)):
        place=int(input('Enter place where mark has to be placed : '))

    return place


def replay():
    playAgain = input('Want to play again ? Y or N')
    return playAgain.lower()

print('=======================')
print('Welcome to Tic Tac Toe!')
print('=======================')

while True:
    Board = [' ']*10
    display_board(Board)
    Player1_Sign = player_input()
    if(Player1_Sign == 'X'):
        Player2_Sign = 'O'
    if(Player1_Sign == 'O'):
        Player2_Sign = 'X'
    GameTurn = choose_first()
    print(GameTurn+' Plays First')
    while True:
        # Player1's turn.
        if(GameTurn == 'Player1'):
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board,Player1_Sign,position)
            if(win_check(Board,Player1_Sign) == True):
                display_board(Board)
                print('Congratulations! You Won the game')
                break
            else:
                if(full_board_check(Board) == True):
                    print('Game draw')
                    break
                else:
                    GameTurn = 'Player2'
        # Player2's turn.
        else:
            display_board(Board)
            position = player_choice(Board)
            place_marker(Board,Player2_Sign,position)
            if(win_check(Board,Player2_Sign) == True):
                display_board(Board)
                print('Congratulations! You Won the game')
                break
            else:
                if(full_board_check(Board) == True):
                    print('Game draw')
                    break
                else:
                    GameTurn = 'Player1'

    if not replay():
        break