import os
os.system('clear')

# list_num = [1.1, 1.2, 3.1, 5, 10.01]
# res_list = []
# for i in list_num:
#     if not i % 1 == 0:
#         res_list.append(round(i % 1, 2))
# print(list_num, '=>', max(res_list) - min(res_list), end='\n\n')

# Ваше решение, которое я немного доработал:

lst = [1.1, 1.2, 3.1, 5, 10.01]

# пришлось добавить условие 'if not val%1 == 0' т.к. не совсем корректно работала программа при наличии целых чисел в списке
res = [round(val % 1, 2) for val in lst if not val%1 == 0]
print(lst, '=>', max(res) - min(res))