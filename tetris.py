import random
import time
import os

# Define the shapes of the blocks and their rotations
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 0], [1, 1, 1]],  # T shape
    [[1, 1, 0], [0, 1, 1]],  # S shape
    [[0, 1, 1], [1, 1, 0]]   # Z shape
]

# Game parameters
BOARD_WIDTH = 10
BOARD_HEIGHT = 20
TICK_TIME = 0.5  # Time interval between each tick

# Initialize the game board
def create_board():
    return [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

# Draw the game board and piece
def draw_board(board, piece, offset):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell or (piece and 
                        y >= offset[1] and 
                        y < offset[1] + len(piece) and 
                        x >= offset[0] and 
                        x < offset[0] + len(piece[0]) and 
                        piece[y - offset[1]][x - offset[0]]):
                print('■', end=' ')
            else:
                print(' ', end=' ')
        print()
    print('\nControls: a - left, d - right, s - down, w - rotate, q - quit')

# Check if the piece can be placed at the given position
def valid_position(board, piece, offset):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                if (y + offset[1] >= len(board) or 
                    x + offset[0] >= len(board[0]) or 
                    x + offset[0] < 0 or 
                    board[y + offset[1]][x + offset[0]]):
                    return False
    return True

# Merge the piece into the board
def join_matrixes(board, piece, offset):
    for y, row in enumerate(piece):
        for x, cell in enumerate(row):
            if cell:
                board[y + offset[1]][x + offset[0]] = cell
    return board

# Clear full lines
def clear_lines(board):
    new_board = [row for row in board if any(cell == 0 for cell in row)]
    new_board = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT - len(new_board))] + new_board
    return new_board

# Rotate the piece
def rotate(piece):
    return [list(row) for row in zip(*piece[::-1])]

# Game loop
def tetris():
    board = create_board()
    piece = random.choice(SHAPES)
    piece_x = BOARD_WIDTH // 2 - len(piece[0]) // 2
    piece_y = 0

    while True:
        # Check for game over condition (if piece starts above the board)
        if not valid_position(board, piece, (piece_x, piece_y)):
            print("Game Over!")
            break

        draw_board(board, piece, (piece_x, piece_y))
        time.sleep(TICK_TIME)
        piece_y += 1
        if not valid_position(board, piece, (piece_x, piece_y)):
            piece_y -= 1
            board = join_matrixes(board, piece, (piece_x, piece_y))
            board = clear_lines(board)
            piece = random.choice(SHAPES)
            piece_x = BOARD_WIDTH // 2 - len(piece[0]) // 2

        # User controls for moving and rotating
        user_input = input()
        if user_input == 'a':
            if valid_position(board, piece, (piece_x - 1, piece_y)):
                piece_x -= 1
        elif user_input == 'd':
            if valid_position(board, piece, (piece_x + 1, piece_y)):
                piece_x += 1
        elif user_input == 's':
            # Move piece down faster
            if valid_position(board, piece, (piece_x, piece_y + 1)):
                piece_y += 1
        elif user_input == 'w':
            rotated_piece = rotate(piece)
            if valid_position(board, rotated_piece, (piece_x, piece_y)):
                piece = rotated_piece
        elif user_input == 'q':
            print("Thanks for playing!")
            break

# Start the game
if __name__ == "__main__":
    tetris()