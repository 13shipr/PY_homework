# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

import os
os.system('clear')

with open('polynom_1.txt', 'r') as file:
    poly_1 = file.readline()

with open('polynom_2.txt', 'r') as file:
    poly_2 = file.readline()

print(f'{poly_1}+{poly_2}')

with open('polynom_sum.txt', 'w') as file:
    file.write((f'{poly_1}+{poly_2}'))