from random import choice
from ada import TicTac

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

play = TicTac()
class AiPlayer:
    def __init__(self, vine, positions: list[int]):
        self.positions = positions
        self.human = vine
        self.mark = 'O'
        self.play = TicTac()
        self.barcus_rec = []

    def best_move(self, board):
        marcus = choice(self.positions)
        best_score = -float('inf')
        move = None
        joe = ''
        for _ in self.positions:
            self.play(vine=marcus, player_rec=self.barcus_rec, mark=self.mark)
            score = self.minimax(board, 0, False)
            self.play(vine=marcus, player_rec=self.barcus_rec, mark=joe)
            if score > best_score:
                best_score = score
                move = _
        return move

    def minimax(self, board, depth, is_maximizing):
        if is_winner(self.marcus, board):
            return 1
        elif is_winner(self.human, board):
            return -1
        elif is_draw(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = self.marcus
                        score = self.minimax(board, depth - 1, False)
                        board[row][col] = " "
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == " ":
                        board[row][col] = self.human
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = " "
                        best_score = min(score, best_score)
            return best_score


