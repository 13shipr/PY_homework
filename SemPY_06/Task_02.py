import random as r
import os
os.system('clear')

# num = random.randint(4, 6)
# num_list = []
# result_list = []
# for i in range(num):
#     num_list.append(random.randint(2, num*2))
# for i in range(num):
#     if (i >= num-i):
#         break
#     result_list.append(num_list[i]*num_list[num-1-i])
# print(num_list, '=>', result_list)

lst = [r.randint(0, 10) for i in range(r.randint(6, 10))]
res = list((map(lambda i: lst[i] * lst[len(lst) - i - 1], range(len(lst) // 2 + len(lst) % 2))))
print(lst, '=>', res)