import random as r
import os
os.system('clear')

# size = int(input('ввведите количество элементов в списке: '))
# num_list = list(range(1, size+1))
# result = 0
# for i in range(len(num_list)):
#     if not i %2:
#         result += num_list[i]
# print(num_list, '=>', result)

lst = [r.randint(0, 10) for i in range(r.randint(6, 10))]
print(lst, '=>', sum([x for y, x in enumerate(lst) if not y % 2 == 0]))
