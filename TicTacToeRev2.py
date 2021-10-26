import os
from winsound import Beep

availability = False
player = 'X'
counter = 0

board = [str(i) for i in range(1, 10)]


def check_draw(draw):
    global x
    if(draw == 9):
        x = True


def check(board_position):
    if (board_position == 'X') or (board_position == 'O'):
        print('***block in use***')
        return False

    return True


def victory_check(x):
    global counter

    if (board[0] == player):
        if (board[1] == player):
            if (board[2] == player):
                print("Player win: ", player)
                return True
    if (board[3] == player):
        if (board[4] == player):
            if (board[5] == player):
                print("Player win: ", player)
                return True
    if (board[6] == player):
        if (board[7] == player):
            if (board[8] == player):
                print("Player win: ", player)
                return True
    if (board[0] == player):
        if (board[4] == player):
            if (board[8] == player):
                print("Player win: ", player)
                return True
    if (board[2] == player):
        if (board[4] == player):
            if (board[6] == player):
                print("Player win: ", player)
                return True
    if (board[0] == player):
        if (board[3] == player):
            if (board[6] == player):
                print("Player win: ", player)
                return True
    if (board[2] == player):
        if (board[5] == player):
            if (board[8] == player):
                print("Player win: ", player)
                return True
    if (board[1] == player):
        if (board[4] == player):
            if (board[7] == player):
                print("Player win: ", player)
                return True
    if (counter == 9):
        print('!!!DRAW!!!')
        return True


def include_table_position(position):
    global availability
    global counter

    if (1 <= position <= 9):
        availability = check(board[position - 1])
        if (availability):
            board[position - 1] = player
            counter += 1
    else:
        print('***Enter a valid number....***')


def show_board():
    print(board[0], '|', board[1], '|', board[2],)
    print('--|---|---')
    print(board[3], '|', board[4], '|', board[5],)
    print('--|---|---')
    print(board[6], '|', board[7], '|', board[8],)
    print('\nType ~0~ to exit')


while (True):
    show_board()
    try:
        position = int(
            input('Which position do you want to place: *{}* '.format(player)))
        if (position == 0):
            for i in range(2):
                Beep(500, 200)
            print("Exit -- Bye")
            input('Press any key')
            Beep(3000, 100)
            break

        os.system('cls')
        include_table_position(position)
        Beep(2000, 50)
        x = victory_check(position)
        check_draw(counter)
        if (x == True):
            for i in range(2):
                Beep(1000, 50)
            Beep(1000, 200)
            break
        if (availability):
            if (player == 'X'):
                player = 'O'
            elif (player == 'O'):
                player = 'X'
    except:
        for i in range(5):
            Beep(3000, 25)
        print("Just type numbers")
