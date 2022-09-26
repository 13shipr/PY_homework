# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# import os 
# os.system('clear')

x, y, z = range(2), range(2), range(2)
if not (x or y or z) == (not x and not y and not z):
    print('истина', end='\n\n')
else:
    print('ложь')