# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# import os 
# os.system('clear') # для Mac

x = int(input('введите значение по оси X: ', ))
y = int(input('введите значения по оси Y: ', ))
if x > 0 and y > 0:
    print('четверть - I', end='\n')
if x < 0 and y > 0:
    print('четверть - II', end='\n')
if x < 0 and y < 0:
    print('четверть - III', end='\n')
if x > 0 and y < 0:
    print('четверть - IV', end='\n')