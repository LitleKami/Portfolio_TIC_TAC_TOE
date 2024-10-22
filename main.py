import itertools
from random import choice


one, two, three = [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']
winning_combos = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [2, 5, 8], [3, 6, 9], [3, 5, 7], [4, 5, 6], [7, 8, 9],
       [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1],
      [1, 4, 7], [1, 7, 4], [4, 1, 7], [4, 7, 1], [7, 1, 4], [7, 4, 1],
      [1, 5, 9], [1, 9, 5], [5, 1, 9], [5, 9, 1], [9, 1, 5], [9, 5, 1],
      [2, 5, 8], [2, 8, 5], [5, 2, 8], [5, 8, 2], [8, 2, 5], [8, 5, 2],
      [3, 6, 9], [3, 9, 6], [6, 3, 9], [6, 9, 3], [9, 3, 6], [9, 6, 3],
      [3, 5, 7], [3, 7, 5], [5, 3, 7], [5, 7, 3], [7, 3, 5], [7, 5, 3],
      [4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 4, 5], [6, 5, 4],
      [7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 7, 8], [9, 8, 7]]
board = ['']*9

def win_checker(combo: list, winning_combos, player):
    # Generate all combinations
    combinations = list(itertools.combinations(combo, 3))
    # Check if any combination from combo exists in winning combos

    for combo in winning_combos:
        if combo in combinations:
            return False
        return True


def is_board_full(board):
    return "Not in board"



def update_board(vine, player_rec, mark, positions, board):

    if int(vine) in positions:
        if int(vine) <= 3:
            one[int(vine) - 1] = mark
        elif int(vine) < 7:
            two[int(vine) - 4] = mark
        else:
            three[int(vine) - 7] = mark
        board[int(vine)] = mark
        positions.remove(int(vine))
        player_rec.append(vine)
        print(f"{one[0]}|{one[1]}|{one[2]}")
        print("-----")
        print(f"{two[0]}|{two[1]}|{two[2]}")
        print("-----")
        print(f"{three[0]}|{three[1]}|{three[2]}")
    player_rec = [num for num in player_rec if type(num) is int]
    print(player_rec)
    print(f"Positions left: {positions}")
    # print(win_checker(player_rec, winning_combos=winning_combos))


def tic_tac_toe(winning_combos):
    # Intro
    print('Litle_kami Games')
    print('TIC TAC TOE')
    board = ['']*9
    print(f"{one[0]}|{one[1]}|{one[0]}")
    print("-----")
    print(f"{two[0]}|{two[1]}|{two[2]}")
    print("-----")
    print(f"{three[0]}|{three[1]}|{three[2]}")
    # game on
    player_rec = []
    barcus_rec = []
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game = True
    print('Welcome to Tic Tac Toe')
    player_name = input('Please insert your name.  ')
    player = 'X'
    print("How to play: The positions are numbered 1 to 9 from left to right in threes.That is top three boxes are "
          "accessed by 1, 2, 3 respectively, the middle boxes are accessed by 4, 5, 6 while the bottom three boxes "
          "are accessed by 7, 8, and 9. Remember, you are player 'X' Goodluck!!")

    while game:
        try:
            vine = int(input('Your Turn:   '))
            if vine not in positions:
                raise ValueError
        except ValueError:
            print(f'Invalid input: Please input integers from this list {positions}')
        else:
            human_mark = "X"
            board[vine - 1] = 'X'
            update_board(vine, player_rec, mark=human_mark, positions=positions, board=board)
            if len(player_rec) >= 3 and win_checker(player_rec, winning_combos, player='X') == False:
                print(f"Congratulations {player_name}, you won!!")
                game = False
            else:
                try:
                    bar_play = ai_move(board)
                except IndexError:
                    print('Draw!!!')
                    game = False
                else:
                    print(f"Barcus played: {bar_play}")
                    barcus_rec.append(bar_play)
                    marcus_mark = 'O'
                    update_board(vine=str(bar_play), player_rec=barcus_rec, mark=marcus_mark, positions=positions,
                                 board=board)
                    if len(barcus_rec) >= 3 and win_checker(barcus_rec, winning_combos, player='O') == False:
                        print("You Lose!! ")
                        game = False

    play_again = input('Would you like to play another round. YES or NO:   ').lower()
    try:
        if play_again == 'yes':
            tic_tac_toe(winning_combos)
        elif play_again == 'no':
            return 'See you next time'
    except ValueError:
        return 'oh! oh! Wrong input'


if __name__ == '__main__':
    tic_tac_toe(winning_combos)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
