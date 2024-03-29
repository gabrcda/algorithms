import random


def make_boards():
    game_board = ["#" for _ in range(24)]
    board_empty = game_board.copy()

    return game_board, board_empty

def populate_board_game(board):
    symbols = ["x", "o", "#", "+", "-", "@"]
    cells = [n for n in range(24)]
    unsorted_cells = []
    
    for i in range(24):
        number = random.sample(cells, 1)
        unsorted_cells.append(number[0])
        board[unsorted_cells[i]] = symbols[int(i/6)]
        cells.remove(number[0])
        
    print(unsorted_cells)
    print(board)



if __name__ == "__main__":
    game_board, board_empty = make_boards()
    # print(game_board)
    # print(board_empty)
    populate_board_game(game_board)