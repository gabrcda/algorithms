import random

NPC_PLAYER = "O"
HUMAN_PLAYER = "X"

def create_board():
    return [n for n in range(9)]

def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
    print("*" *50)

def check_empty_cell(board, cell):
    return type(board[cell]) == int

def check_draw(board):
    return all(isinstance(elem, str) for elem in board)

def check_winner(board):
    for i in range(0, 9, 3):
        if (board[i] == board[i+1] == board[i+2]): return (True, board[i])

    for i in range(3):
        if (board[i] == board[i+3] == board[i+6]): return (True, board[i])

    if (board[0] == board[4] == board[8]): return (True, board[0])
    if (board[2] == board[4] == board[6]): return (True, board[2])
    return False, None

def random_cell_play():
    return random.randrange(0, 9)

def choose_initial_player():
    return random.choice([NPC_PLAYER, HUMAN_PLAYER])

def human_play():
    return int(input("Enter the cell: "))

def insert_play(current_player, board, cell):
    board[cell] = current_player
    if (current_player == HUMAN_PLAYER):
        return NPC_PLAYER
    else:
        return HUMAN_PLAYER


if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
    current_player = choose_initial_player()
    
    while True:
        cell = random_cell_play() if current_player == NPC_PLAYER else human_play()

        while(not check_empty_cell(game_board, cell)):
            cell = random_cell_play() if current_player == NPC_PLAYER else human_play()

        current_player = insert_play(current_player, game_board, cell)
        print_board(game_board)
        situation, player = check_winner(game_board)

        if (situation):
            print(f"The Winner is '{player}'")
            break
        situation = check_draw(game_board)
        if (situation):
            print("Game Draw")  
            break