# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import pi
import os
os.system('clear')

d = 0.001
print(round(pi, (len(str(d).replace('.', ''))-1)))
