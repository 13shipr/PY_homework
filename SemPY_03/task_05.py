# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

import os
os.system('clear')

num = int(input('введите число: '))
fibo_list = [0]
count = 1
if num > 0:
    num_list = [1, 0, 1]
while count < num:
    num_list.append((num_list[len(num_list) - 1]) +
                    num_list[len(num_list) - 2])
    if count % 2 == 0:
        num_list.insert(0, num_list[len(num_list) - 1])
    else:
        num_list.insert(0, -num_list[len(num_list) - 1])
    count += 1
print(num_list, end='\n\n')
