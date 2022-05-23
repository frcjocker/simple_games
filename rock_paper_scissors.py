from random import randint

d = {0: 'Rock', 1: 'Paper', 2: 'Scissor'}

def comp_choice(minimum: int, maximum: int) -> int:
    l = randint(minimum, maximum)
    print(f'Computer choosed = {d[l]}')
    return l

def player_choice() -> int:
    for i in range(len(d)):
        print(f'{i}: {d[i]}')
    l = int(input(f'please choose'))
    print(f'Player choosed = {d[l]}')
    return l

def winner(comp: int, player: int) -> int:
    if comp == player:
        return 0
    if comp == player + 1 or (comp == 0 and player == 2):
        return 2
    else:
        return 1

def rps_game():
    score = [0, 0]
    print('Rock Paper Scissors game START!')
    answer = ''
    while answer != 'n':
        x1 = player_choice()
        x2 = comp_choice(0, 2)
        result = winner(x2, x1)
        if result == 0:
            print("Its a tie")
        elif result == 2:
            print("computer won!")
            score[1] += 1
        else:
            print("player won!")
            score[0] += 1
        print(f'Player vs Computer: {score[0]} : {score[1]}')
        answer = input('Do you wonna play again? Yes - y, No - n')