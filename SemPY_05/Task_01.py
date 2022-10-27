# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import os
os.system('clear')

text = 'Съешь ещёабв этих мягабвких французских булок, да выпей жеабв чаю'
lst = text.split()
for item in lst:
    if 'абв' in item:
        lst.remove(item)
print(lst)