
board = ['-'] * 9

HUMAN = 'X'
AI = 'O'


winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]

def display_board():
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])

def evaluate_board():
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != '-':
            return 1 if board[combo[0]] == AI else -1
    return 0

def is_board_full():
    return '-' not in board

def minimax(depth, is_maximizing):
    if evaluate_board() == 1:
        return 1
    if evaluate_board() == -1:
        return -1
    if is_board_full():
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = AI
                score = minimax(depth + 1, False)
                board[i] = '-'
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == '-':
                board[i] = HUMAN
                score = minimax(depth + 1, True)
                board[i] = '-'
                best_score = min(best_score, score)
        return best_score

def find_best_move():
    best_move = -1
    best_score = float('-inf')
    for i in range(9):
        if board[i] == '-':
            board[i] = AI
            score = minimax(0, False)
            board[i] = '-'
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def main():
    while not is_board_full():
        display_board()
        
        human_move = int(input("Enter your move (0-8): "))
        if board[human_move] == '-':
            board[human_move] = HUMAN
        else:
            print("Invalid move. Try again.")
            continue
        
        if evaluate_board() == -1:
            print("You win!")
            break
        
        ai_move = find_best_move()
        board[ai_move] = AI
        
        if evaluate_board() == 1:
            display_board()
            print("AI wins!")
            break
        
    if is_board_full() and evaluate_board() == 0:
        display_board()
        print("It's a draw!")

if __name__ == "__main__":
    main()
