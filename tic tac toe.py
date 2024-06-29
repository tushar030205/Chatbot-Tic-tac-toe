import math

# Initialize the board
def initialize_board():
    return [' ' for _ in range(9)]

# Print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Check for a win
def check_winner(board, player):
    win_conditions = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conditions

# Check for a draw
def check_draw(board):
    return ' ' not in board

# Get available moves
def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot == ' ']

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for move in get_available_moves(board):
            board[move] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_available_moves(board):
            board[move] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Best move for AI
def best_move(board):
    best_eval = -math.inf
    move = None
    for m in get_available_moves(board):
        board[m] = 'O'
        eval = minimax(board, 0, False, -math.inf, math.inf)
        board[m] = ' '
        if eval > best_eval:
            best_eval = eval
            move = m
    return move

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe! You are X, and the AI is O.")
    print_board(board)
    
    while True:
        # Player move
        while True:
            move = int(input("Enter your move (0-8): "))
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("Invalid move. Try again.")
        
        print_board(board)
        
        if check_winner(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        
        # AI move
        move = best_move(board)
        board[move] = 'O'
        print("AI plays:")
        print_board(board)
        
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

# Start the game
play_game()
