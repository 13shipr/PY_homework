# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter = int(input('введите номер четверти: '))
if quarter == 1:
    print('x > 0, y > 0', end='\n')
if quarter == 4:
    print('x > 0, y < 0', end='\n')
if quarter == 3:
    print('x < 0, y < 0', end='\n')
if quarter == 2:
    print('x < 0, y > 0', end='\n')