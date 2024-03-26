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

def evaluate(board):
    for i in range(0, 9, 3):
        if (board[i] == board[i+1] == board[i+2] == NPC_PLAYER):
            return 10
        elif (board[i] == board[i+1] == board[i+2] == HUMAN_PLAYER):
            return -10

    for i in range(3):
        if (board[i] == board[i+3] == board[i+6] == NPC_PLAYER):
            return 10
        elif (board[i] == board[i+3] == board[i+6] == HUMAN_PLAYER):
            return -10

    if (board[0] == board[4] == board[8] == NPC_PLAYER) or (board[2] == board[4] == board[6] == NPC_PLAYER):
        return 10
    elif (board[0] == board[4] == board[8] == HUMAN_PLAYER) or (board[2] == board[4] == board[6] == HUMAN_PLAYER):
        return -10

    return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if check_empty_cell(board, i):
                board[i] = NPC_PLAYER
                score = minimax(board, depth + 1, False)
                board[i] = i
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if check_empty_cell(board, i):
                board[i] = HUMAN_PLAYER
                score = minimax(board, depth + 1, True)
                board[i] = i
                best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float("inf")
    best_move = -1

    for i in range(9):
        if check_empty_cell(board, i):
            board[i] = NPC_PLAYER
            score = minimax(board, 0, False)
            board[i] = i
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

if __name__ == "__main__":
    game_board = create_board()
    print_board(game_board)
    current_player = choose_initial_player()
    
    while True:
        cell = best_move(game_board) if current_player == NPC_PLAYER else human_play()

        while(not check_empty_cell(game_board, cell)):
            cell = best_move(game_board) if current_player == NPC_PLAYER else human_play()

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
