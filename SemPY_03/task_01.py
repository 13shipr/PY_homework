# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
os.system('clear')

size = int(input('ввведите количество элементов в списке: '))
num_list = list(range(1, size+1))
result = 0
for i in range(len(num_list)):
    if not i %2:
        result += num_list[i]
print(num_list, '=>', result)