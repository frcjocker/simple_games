from random import choice

def draw_square(t):
    print('  1 2 3')
    for i in range(3):
        a = f'{i+1}'
        for j in range(3):
            a += ' ' + str(t[i][j])
        print(a)

def comp_choice(t):
    a = []
    for i in range(3):
        for j in range(3):
            if t[i][j] not in 'OX':
                a.append(f'{i}{j}')
    l = choice(a)
    t[int(l[0])][int(l[1])] = 'X'
    return t

def player_choice(t):
    while True:
        i = int(input("Введите номер строки, в который вы хотите сходить: ")) - 1
        j = int(input("Введите номер столбца, в который вы хотите сходить: ")) - 1
        if t[i][j] not in 'XO':
            t[i][j] = 'O'
            break
        else:
            print("Введите заново")
    return t

def check_winner(t):
    a = []
    for i in range(3):
        a.append(''.join(t[i]))
        a.append(''.join(t[j][i] for j in range(3)))
    a.append(''.join(t[j][j] for j in range(3)))
    a.append(''.join(t[j][2-j] for j in range(3)))
    if 'XXX' in a:
        return 'X'
    elif 'OOO' in a:
        return 'O'
    else:
        return '-'

def play():
    start_massive = [['-' for _ in range(3)] for _ in range(3)]
    draw_square(start_massive)
    winner = '-'
    step = 0
    while winner == '-' and step <= 8:
        if step%2 == 0:
            start_massive = comp_choice(start_massive)
            step += 1
        else:
            player_choice(start_massive)
            step += 1
        draw_square(start_massive)
        winner = check_winner(start_massive)
    if winner == '-':
        print('It is a tie')
        return '-'
    elif winner == 'X':
        print('The winner is computer')
        return 'X'
    else:
        print('The winner is player')
        return 'O'

def tic_tac_game():
    answer = ''
    score = [0, 0]
    while answer != 'n':
        result = play()
        if result == 'X':
            score[1] += 1
        if result == 'O':
            score[0] += 1
        print(f'Score value: Player vs Computer - {score[0]} : {score[1]}')
        answer = input("Do you want to play again?\n Yes - y, No - n: ")