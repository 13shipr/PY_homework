# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

from os import system
system('clear')

# решение через замену и преведением к целым числам

# num = str((input('введите число: ')))
# str_num = num.replace(',', '')
# list_num = list(str_num)
# list_int = map(int, list_num)
# print('сумма цифр в числе =', sum(list_int))

# # решение через разделение, преведением к целым числам сумма через цикл

# num = str(input('введите число: '))
# d_split = num.split(',')
# d_int = int(d_split[0])
# d_double = int(d_split[1])
# d_sum = 0
# while(d_int !=0):
#     d_sum = d_sum + (d_int%10)
#     d_int = d_int//10
# while(d_double !=0):
#     d_sum = d_sum + (d_double%10)
#     d_double = d_double//10
# print(d_sum)

# через isdigit

num = input('введите число: ')
res = 0
for i in num:
    if num.isdigit():
        res += int(i)
print(res)