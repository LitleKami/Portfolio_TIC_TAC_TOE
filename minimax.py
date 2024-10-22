import  random

def win_checker(board, mark):
    pass

def is_board(board):
    pass


def minimax(board, depth, is_maximizing):
    if win_checker(board, 'X'):
        return 10
    elif win_checker(board, 'O'):
        return -10
    elif is_board(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if board[i] == '':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ''
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if board[i] == '':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ''
                best_score = min(score, best_score)
        return best_score


def ai_move(board):
    best_score = -1000
    best_move = 0
    for i in range(9):
        if board[i] == '':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ''
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

