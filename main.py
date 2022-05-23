from tic_tac_toe import tic_tac_game
from rock_paper_scissors import rps_game
from tic_tac_toe2 import tic_tac_toe2

choices = ['Tic tac toe', 'Rock paper scissors', 'Tic tac toe 2']

if __name__ == '__main__':
    player_choice = ''
    while player_choice != 'n':
        for i in range(len(choices)):
            print(f'Game number #{i}: {choices[i]}')
        player_choice = input('What game you wonna play? If you don"t wonna play press "n"')
        if player_choice == '0':
            tic_tac_game()
        elif player_choice == '1':
            rps_game()
        elif player_choice == '2':
            tic_tac_toe2()