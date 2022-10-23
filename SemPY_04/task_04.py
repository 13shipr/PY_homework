# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import os
os.system('clear')

k = int(input('Введите натуральную степень k:'))
def poly(k):
    koeff = [randint(0, 100) for i in range(k)]+[randint(1, 100)]
    polynom = '+'.join([f'{(elem,"")[elem==1]}x**{i}' for i,
                    elem in enumerate(koeff) if elem][::-1])
    polynom = polynom.replace('x**1+', 'x+')
    polynom = polynom.replace('x**0', '')
    polynom += ('', '1')[polynom[-1] == '+']
    polynom = (polynom, polynom[:-2])[polynom[-2:] == '**1']
    return polynom

print(poly(k))

with open('polynom_1.txt', 'w') as file:
    file.write(f'{poly(k)}')

with open('polynom_2.txt', 'w') as file:
    file.write(f'{poly(randint(1, 5))}')