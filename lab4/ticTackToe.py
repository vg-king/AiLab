# Tic Tac Toe Game - Simple Python Implementation

def print_board(board):
    """Display the game board"""
    print("\n")
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---|---|---")
    print("\n")


def check_winner(board, player):
    """Check if player has won"""
    # Win conditions: rows, columns, diagonals
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_board_full(board):
    """Check if board is full (draw)"""
    return all(cell in ['X', 'O'] for cell in board)


def get_move(board, player):
    """Get valid move from player"""
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] not in ['X', 'O']:
                return move
            else:
                print("Invalid move! Position taken or out of range.")
        except (ValueError, IndexError):
            print("Invalid input! Enter a number between 1-9.")


def get_ai_move(board):
    """AI makes a move using simple strategy"""
    import random
    
    # 1. Try to win
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            if check_winner(board, 'O'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # 2. Block opponent's winning move
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            if check_winner(board, 'X'):
                board[i] = ' '
                return i
            board[i] = ' '
    
    # 3. Take center if available
    if board[4] == ' ':
        return 4
    
    # 4. Take a corner
    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] == ' ']
    if available_corners:
        return random.choice(available_corners)
    
    # 5. Take any available space
    available = [i for i in range(9) if board[i] == ' ']
    return random.choice(available) if available else None


def play_game():
    """Main game loop"""
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    current_player = 'X'
    
    print("="*40)
    print("     TIC TAC TOE GAME")
    print("="*40)
    print("\nPositions:")
    print_board(board)
    
    # Reset board for game
    board = [' '] * 9
    
    while True:
        print_board(board)
        
        # Get move (Human or AI)
        if current_player == 'X':
            move = get_move(board, current_player)
        else:  # AI's turn (Player O)
            print("AI (O) is thinking...")
            import time
            time.sleep(0.5)
            move = get_ai_move(board)
            print(f"AI chose position {move + 1}")
        
        board[move] = current_player
        
        # Check for winner
        if check_winner(board, current_player):
            print_board(board)
            if current_player == 'X':
                print(f" You win!")
            else:
                print(f" AI wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print(" It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == "__main__":
    while True:
        play_game()
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break
