# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import os
os.system('clear')

# list_num = [1.1, 1.2, 3.1, 5, 10.01]
# res_list = []
# for i in list_num:
#     if not i % 1 == 0:
#         res_list.append(round(i % 1, 2))
# print(list_num, '=>', max(res_list) - min(res_list), end='\n\n')


lst = [1.1, 1.2, 3.1, 5, 10.01]
lst = [round(val % 1, 2) for val in lst if not val%1 == 0]
rev_result = max(lst) - min(lst)
print(rev_result)
