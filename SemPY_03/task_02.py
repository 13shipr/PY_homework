# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
import os
os.system('clear')

num = random.randint(4, 6)
num_list = []
result_list = []
for i in range(num):
    num_list.append(random.randint(2, num*2))
for i in range(num):
    if (i >= num-i):
        break
    result_list.append(num_list[i]*num_list[num-1-i])
print(num_list, '=>', result_list)


