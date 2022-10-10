import os
os.system('clear')

num = int(input('ввведите N: '))
num_dict = dict()
for i in range(1, num+1):
    num_dict [i] = round((1+1/i)**i)
result = 0
for i in num_dict:
    result += num_dict[i]
print(num_dict, '=>', result)