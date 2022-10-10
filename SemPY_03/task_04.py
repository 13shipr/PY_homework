# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

import os
os.system('clear')

num = int(input('введите число: '))
print(f'{bin(num)[2:]}', end='\n\n')

# или так

num_bin = ''
while not num == 0:
    num_bin += str(num % 2)
    num //= 2
print(num, '=>', num_bin)
