# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('clear')

num = int(input('ввведите N: '))
list_num = list()
n = 1
for i in range(num):
    n = n*(i+1)
    list_num.append(n)
print(list_num)

