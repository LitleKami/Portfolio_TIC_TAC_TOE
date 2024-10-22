
import itertools
from random import choice

one, two, three = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
board = [' '] * 9

def check_winner(board):
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def is_board_full(board):
    return ' ' not in board

def update_board(vine, mark, board):
    board[int(vine) - 1] = mark
    display_board(board)

def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def ai_move(board):
    best_score = float('-inf')
    move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i + 1  # Return the move in 1-indexed format
    return move

def tic_tac_toe():
    board = [' '] * 9
    print('Welcome to Tic Tac Toe')
    player_name = input('Please insert your name: ')
    display_board(board)
    game = True

    while game:
        try:
            vine = int(input('Your Turn (1-9): '))
            if vine not in range(1, 10) or board[vine - 1] != ' ':
                raise ValueError
        except ValueError:
            print('Invalid input. Try again.')
            continue

        update_board(vine, 'X', board)

        if check_winner(board) == 'X':
            print(f"Congratulations {player_name}, you won!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        bar_play = ai_move(board)
        print(f"Barcus played: {bar_play}")
        update_board(bar_play, 'O', board)

        if check_winner(board) == 'O':
            print("You Lose!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

    if input('Would you like to play another round? (yes/no): ').lower() == 'yes':
        tic_tac_toe()
    else:
        print('See you next time!')


if __name__ == '__main__':
    tic_tac_toe()


