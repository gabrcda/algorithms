import random


def make_boards():
    game_board = ["#" for _ in range(24)]
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


if __name__ == "__main__":
    game_board, empty_board = make_boards()
    # print(game_board)
    # print(board_empty)
    game_board = populate_board_game(game_board)