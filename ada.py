import itertools
from random import random, choice

board = (' | | \n'
         ' | | \n'
         ' | | ')

print(list(board)[2])

winning_combos = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9],
       [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1],
      [1, 4, 7], [1, 7, 4], [4, 1, 7], [4, 7, 1], [7, 1, 4], [7, 4, 1],
      [1, 5, 9], [1, 9, 5], [5, 1, 9], [5, 9, 1], [9, 1, 5], [9, 5, 1],
      [2, 5, 8], [2, 8, 5], [5, 2, 8], [5, 8, 2], [8, 2, 5], [8, 5, 2],
      [3, 6, 9], [3, 9, 6], [6, 3, 9], [6, 9, 3], [9, 3, 6], [9, 6, 3],
      [3, 5, 7], [3, 7, 5], [5, 3, 7], [5, 7, 3], [7, 3, 5], [7, 5, 3],
      [4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 4, 5], [6, 5, 4],
      [7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 7, 8], [9, 8, 7]]


class TicTac:
    def __init__(self, winning_combos):
        self.one = ['', '', '']
        self.two = ['', '', '']
        self.three = ['', '', '']
        self.winning_combos = winning_combos
        self.positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.game = True
        self.play()

    def win_checker(self, combo: list[int]):
        # Generate all combinations
        combinations = list(itertools.combinations(combo, 3))
        # Check if any combination from combo exists in winning combos
        for combo in combinations:
            if list(combo) in self.winning_combos:
                self.game = False
                return self.game

    def vinee(self, vine, player_rec, mark):
        if int(vine) in self.positions:
            if int(vine) <= 3:
                self.one[int(vine) - 1] = mark
            elif int(vine) < 7:
                self.two[int(vine) - 4] = mark
            else:
                self.three[int(vine) - 7] = mark
            self.positions.remove(int(vine))
            player_rec.append(vine)
            print(f"{self.one[0]}|{self.one[1]}|{self.one[2]}")
            print("-----")
            print(f"{self.two[0]}|{self.two[1]}|{self.two[2]}")
            print("-----")
            print(f"{self.three[0]}|{self.three[1]}|{self.three[2]}")
        player_rec = [num for num in player_rec if type(num) is int]
        print(player_rec)
        print(f"Positions left: {self.positions}")
        # print(win_checker(player_rec, winning_combos=winning_combos))

    def is_board_full(self, board):
        return "Not in board"

    def barcus(self, positions, barcus_rec):
        bar_play = choice(positions)
        self.vinee(vine=str(bar_play), player_rec=barcus_rec)

    def play(self):
        print(f"{self.one[0]} |{self.one[1]} |{self.one[0]} ")
        print("-----")
        print(f"{self.two[0]} |{self.two[1]} |{self.two[2]} ")
        print("-----")
        print(f"{self.three[0]} |{self.three[1]} |{self.three[2]} ")
        player_rec = []
        barcus_rec = []
        while self.game:
            try:
                vine = int(input('Your Turn:   '))
                if vine not in self.positions:
                    raise ValueError
            except ValueError:
                print(f'Invalid input: Please input integers from this list {self.positions}')
            else:
                human_mark = "X"
                self.vinee(vine, player_rec, mark=human_mark)
                if len(player_rec) >= 3 and self.win_checker(player_rec) == False:
                    print("Congratulations, you won!!")
                    self.game = False
                else:
                    try:
                        bar_play = choice(self.positions)
                    except IndexError:
                        print('Draw!!!')
                        self.game = False
                    else:
                        print(f"Barcus played: {bar_play}")
                        barcus_rec.append(bar_play)
                        marcus_mark = 'O'
                        self.vinee(vine=str(bar_play), player_rec=barcus_rec, mark=marcus_mark)
                        if len(barcus_rec) >= 3 and self.win_checker(barcus_rec) == False:
                            print("You Lose!! ")
                            self.game = False

        play_again = input('Would you like to play another round. YES or NO:   ').lower()
        try:
            if play_again == 'yes':
                TicTac(winning_combos)
            elif play_again == 'no':
                return 'See you next time'
        except ValueError:
            return 'oh! oh! Wrong input'


play = TicTac(winning_combos)
play





