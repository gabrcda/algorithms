import random

NAMES = ["Gabriel", "Raquel", "Rafael", "Moacir", "Rennan", "Rebeca", "Edna", "Fernando"]
ANIMALS = ["Sparrow", "Eagle", "Parrot", "Pigeon", "Owl", "Shark", "Dolphin", "Whale", "Octopus", "Jellyfish", 
           "Lion", "Elephant", "Giraffe", "Zebra", "Kangaroo", "Panda", "Koala", "Platypus", "Penguin", "Hippopotamus"]
OBJECTS = ["Mug","Pencil", "Chair", "Computer", "Mouse", "Headphones", "Bottle", "Key", "Book", "Table", 
           "Glasses","Watch", "Cellphone", "Tablet", "Lamp", "Bag", "Shoes", "Hat", "Umbrella", "Camera"]

def choose_category():
    return random.choice([NAMES, ANIMALS, OBJECTS])

def get_category_name(category):
    if category == NAMES: return "Names"
    elif category == ANIMALS: return "Animals"
    else: return "Objects"

def choose_word(category):
    return category[random.randrange(0, len(category))].lower()

def make_board(word):
    return ["_" for _ in range(len(word))]

def play():
    return input("Letter: ")

def check_letter(word, letter, board):
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                board[i] = char
    return board

def check_win(board):
    if not "_" in board:
        return True
    return False
            
if __name__ == "__main__":
    category = choose_category()
    word = choose_word(category)
    board = make_board(word)
    print(word)
    print(f"{board} : {get_category_name(category)}")
    while True:
        letter = play()
        board = check_letter(word, letter, board)
        print(board)
        if check_win(board):
            print("WINNER!!!!")
            break