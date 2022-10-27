# Создайте программу для игры в 'Крестики-нолики'.

import os
os.system('clear')


def print_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0+i*3], '|', field[1+i*3], '|', field[2+i*3], '|')
        print('-' * 13)
    print('\n')


def move_player(move, symbol):
    pos = field.index(move)
    field[pos] = symbol


def result():
    win = ''
    for i in wins:
        if field[i[0]] == 'X' and field[i[1]] == 'X' and field[i[2]] == 'X':
            win = 'X'
        if field[i[0]] == 'O' and field[i[1]] == 'O' and field[i[2]] == 'O':
            win = 'O'
    return win


field = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

wins = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]

game_over = False
player_1 = True

while not game_over == True:
    print_field(field)
    if player_1 == True:
        symbol = 'X'
        move = int(input('Игрок 1, ходите (1 - 9): '))
    else:
        symbol = 'O'
        move = int(input('Игрок 2, ходите (1 - 9): '))
    move_player(move, symbol)
    win = result()
    if win != '':
        game_over = True
    else:
        game_over = False
    player_1 = not (player_1)

print("Выиграл: ", win)