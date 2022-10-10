# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 

import os
os.system('clear')

size = int(input('ввведите N: '))
num_list = list(range(-size, size+1))
path = 'file.txt'
data = open(path, 'r')
result = 1
for position in data:
    result = num_list[int(position)*result]
data.close()
print(num_list)
print(result)