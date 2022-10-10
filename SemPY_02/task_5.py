import os
os.system('clear')

import random

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mix_list = random.sample(num_list, len(num_list))
print(f'old list => {num_list} \nnew list => {mix_list}')


