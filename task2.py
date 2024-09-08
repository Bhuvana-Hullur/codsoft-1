import random


board = [' ' for _ in range(9)]


def draw_board():
    row1 = '| {} | {} | {} |'.format(board[0], board[1], board[2])
    row2 = '| {} | {} | {} |'.format(board[3], board[4], board[5])
    row3 = '| {} | {} | {} |'.format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()


def check_game_over():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return False


def minimax(depth, is_maximizing):
    result = check_game_over()
    if result:
        if result == 'X':
            return -10
        elif result == 'O':
            return 10
        elif result == 'Tie':
            return 0

    if is_maximizing:
        best_score = -1000
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(depth + 1, False)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(depth + 1, True)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score


def ai_move():
    best_score = -1000
    best_move = 0
    for i in range(len(board)):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'


def game():
    print("You play as X and the AI plays as O.")
    while True:
        draw_board()
        move = input("Enter your move (1-9): ")
        if board[int(move) - 1] != ' ':
            print("Invalid move, try again.")
            continue
        board[int(move) - 1] = 'X'
        result = check_game_over()
        if result:
            draw_board()
            if result == 'X':
                print("You win!")
            elif result == 'O':
                print("AI wins!")
            else:
                print("It's a tie!")
            break
        ai_move()
        result = check_game_over()
        if result:
            draw_board()
            if result == 'X':
                print("You win!")
            elif result == 'O':
                print("AI wins!")
            else:
                print("It's a tie!")
            break

game()