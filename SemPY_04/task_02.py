# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

import os
os.system('clear')

num = int(input('введите число: '))
lst = [(n, int(num / n)) for n in range(1, num) if not num % n]
print(lst)
