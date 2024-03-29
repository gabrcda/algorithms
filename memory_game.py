def make_boards():
    game_board = ["#" for _ in range(25)]
    board_empty = game_board.copy()
    
    return game_board, board_empty

if __name__ == "__main__":
    game_board, board_empty = make_boards()
    print(game_board)
    print(board_empty)