# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

import random as r
import os
os.system('clear')

num_list = []
for i in range(r.randint(5, 10)):
    num_list.append(r.randint(2, r.randint(3, 9)*2))
print(num_list, '=>', set(num_list))

