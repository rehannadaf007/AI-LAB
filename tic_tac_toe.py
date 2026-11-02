import math
import random

# Constants representing the players and empty spaces
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

def print_board(board):
    """Renders the game board to the console."""
    print("\n" + "  +---+---+---+")
    for row in board:
        print("  | " + " | ".join(row) + " |")
        print("  +---+---+---+")
    print()

def check_winner(board):
    """
    Checks the board for a winner.
    Returns +10 if AI wins, -10 if Human wins, and 0 for a tie or ongoing game.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return 10 if board[i][0] == AI else -10
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return 10 if board[0][i] == AI else -10
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return 10 if board[0][0] == AI else -10
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return 10 if board[0][2] == AI else -10

    return 0

def get_empty_cells(board):
    """Returns a list of tuples (row, col) for all available cells."""
    cells = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                cells.append((r, c))
    return cells

def is_board_full(board):
    """Returns True if no empty spaces remain, False otherwise."""
    return len(get_empty_cells(board)) == 0

def minimax(board, depth, is_maximizing, alpha, beta):
    """
    The core Minimax algorithm with Alpha-Beta Pruning.
    """
    score = check_winner(board)

    # Base cases: Terminal state achieved
    if score == 10:
        return score - depth  # Subtract depth to favor quicker wins
    if score == -10:
        return score + depth  # Add depth to favor longer survival
    if is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = AI
            evaluation = minimax(board, depth + 1, False, alpha, beta)
            board[row][col] = EMPTY  # Undo move
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break  # Beta pruning
        return max_eval
    else:
        min_eval = math.inf
        for row, col in get_empty_cells(board):
            board[row][col] = HUMAN
            evaluation = minimax(board, depth + 1, True, alpha, beta)
            board[row][col] = EMPTY  # Undo move
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break  # Alpha pruning
        return min_eval

def find_best_move(board):
    """Evaluates all available moves and returns the optimal choice for the AI."""
    best_value = -math.inf
    best_move = (-1, -1)

    for row, col in get_empty_cells(board):
        board[row][col] = AI
        # Run minimax assuming the next turn belongs to the human (minimizer)
        move_value = minimax(board, 0, False, -math.inf, math.inf)
        board[row][col] = EMPTY  # Undo move

        if move_value > best_value:
            best_value = move_value
            best_move = (row, col)

    return best_move

def main():
    """Main game loop to play Tic-Tac-Toe against the AI agent."""
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    
    print("Welcome to Tic-Tac-Toe! You are 'O' and the AI is 'X'.")
    print_board(board)

    while True:
        # --- Human Turn ---
        empty_cells = get_empty_cells(board)
        if not empty_cells or check_winner(board) != 0:
            break
            
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = move // 3, move % 3
            if (row, col) not in empty_cells:
                print("Invalid move! That cell is taken. Try again.")
                continue
            board[row][col] = HUMAN
        except (ValueError, IndexError):
            print("Invalid input! Please enter a number between 1 and 9.")
            continue

        print_board(board)

        # Check if human won or tied
        if check_winner(board) == -10:
            print("Congratulations! You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        # --- AI Turn ---
        print("AI is calculating the optimal move...")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = AI
        print_board(board)

        # Check if AI won or tied
        if check_winner(board) == 10:
            print("The AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()
