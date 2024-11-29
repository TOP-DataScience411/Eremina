# Написать программу, которая вычисляет сумму всех делителей числа
import math
n = int(input('Введите натуральное число: '))
sumD = 0
for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        sumD = sumD + i
        if i != n // i:
            sumD = sumD + n // i
print(sumD)
# =================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\3.py"
# Введите натуральное число: 50
# 93

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\3.py"
# Введите натуральное число: 5
# 6

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\3.py"
# Введите натуральное число: 8
# 15