import os
import platform
import random
import time

def make_boards():
    game_board = [ x for x in range(24)]
    empty_board = game_board.copy()

    return game_board, empty_board

def populate_board_game(board):
    symbols = ["x", "o", "#", "+", "-", "@"]
    cells = [n for n in range(24)]
    count = 0

    for i in range(24):
        number = random.sample(cells, 1)
        board[number[0]] = symbols[count]
        cells.remove(number[0])
        count = 0 if count >= 5 else count + 1
        
    return board

def get_play():
    cell_1 = int(input("Cell 1: "))
    cell_2 = int(input("Cell 2: "))
    return cell_1, cell_2

def check_match(cell_1, cell_2, board, empty_board):
    if board[cell_1] == board[cell_2]:
        empty_board[cell_1] = board[cell_1]
        empty_board[cell_2] = board[cell_2]

    return empty_board

def check_win(empty_board):
    for e in empty_board:
        if isinstance(e, int):
            return False
    return True

def print_board(empty_board):
    os.system("cls") if platform.system() == "Windows" else os.system("clear")
    for i in range(0, 24, 4):
        print(f"{empty_board[i]} | {empty_board[i+1]} | {empty_board[i+2]} | {empty_board[i+3]}")
        print("_________________")

def print_initial_board(game_board):
    for i in range(0, 24, 4):
        print(f"{game_board[i]} | {game_board[i+1]} | {game_board[i+2]} | {game_board[i+3]}")
        print("_________________")
    time.sleep(20)
    os.system("cls") if platform.system() == "Windows" else os.system("clear")

if __name__ == "__main__":
    game_board, empty_board = make_boards()
    game_board = populate_board_game(game_board)
    print_initial_board(game_board)
    print_board(empty_board)

    while True:
        cell_1, cell_2 = get_play()
        empty_board = check_match(cell_1, cell_2, game_board, empty_board)
        print_board(empty_board)
        if check_win(empty_board):
            print("WINNER!!!")
            break