import random

#Task 1 - make the board
def display_board(board):
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]} ")
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]} ")
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]} ")

#Task 2 - Take player input (Marker)
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#Task 3 - assign to the board
def place_marker(board, marker, position):
    board[position] = marker

#Task 4 - check if someone wins
def win_check(board,marker):
    win_marker = marker * 3
    if board[1] + board[2] + board[3] == win_marker:
        return True
    elif board[4] + board[5] + board[6] == win_marker:
        return True
    elif board[7] + board[8] + board[9] == win_marker:
        return True
    elif board[7] + board[4] + board[1] == win_marker:
        return True
    elif board[8] + board[5] + board[2] == win_marker:
        return True
    elif board[9] + board[6] + board[3] == win_marker:
        return True
    elif board[1] + board[5] + board[9] == win_marker:
        return True
    elif board[7] + board[5] + board[3] == win_marker:
        return True
    else:
        return False

#Task 5 - make a random function.
def chose_first():
    return random.randint(1,2)

#Task 6 - Check if a space on the board is available
def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for element in board:
        if element == " ":
            return False

    return True

def player_choice(board):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        place_position = input("Choose a postion : (1-9) ")
        if place_position.isdigit():
            if int(place_position) in a:
                if space_check(board, int(place_position)) == True:
                    return place_position

def replay():
    another = input("Do you want to play another one ? (y/n)").upper()
    if another == "Y":
        return True
    elif another == "N":
        return False


def game():
    print("Welcome to Tic Tac Toe! ")

    while True:
        main_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player1, player2 = player_input()

        first = chose_first()
        print(f"Player{first} will be first!")

        play_game = input("Should we start? (y/n)").upper()

        if play_game == "Y":
            game_on = True
        else:
            game_on = False

        while game_on:
            if first == 1:
                #Show the board
                display_board(main_board)
                #Chose a position
                position = player_choice(main_board)
                #Place marker
                place_marker(main_board, player1, int(position))
                #check if won
                if win_check(main_board,player1):
                    display_board(main_board)
                    print("PLAYER1 HAS WON!!! ")
                    game_on = False
                else:
                    if full_board_check(main_board):
                        display_board(main_board)
                        print("Nobody Wins -.- ")
                        game_on = False
                    else:
                        first = 2
            else:
                display_board(main_board)
                position = player_choice(main_board)
                place_marker(main_board, player2, int(position))
                if win_check(main_board, player2):
                    display_board(main_board)
                    print("PLAYER2 HAS WON!!! ")
                    game_on = False
                else:
                    if full_board_check(main_board):
                        display_board(main_board)
                        print("Nobody Wins -.- ")
                        game_on = False
                    else:
                        first = 1

        if not replay():
            break

game()
