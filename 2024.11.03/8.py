# Написать программу, которая выводит требуемое количество чисел последовательности Фибоначчи
n = int(input('Введите натуральное число - кол-во чисел Фибоначчи: '))
lst_fib = [1, 1]
for i in range(2, n):
    lst_fib.append(lst_fib[i - 2] + lst_fib[i - 1])
print(*lst_fib, sep=' ')
# ========================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\8.py"
# Введите натуральное число - кол-во чисел Фибоначчи: 17
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\8.py"
# Введите натуральное число - кол-во чисел Фибоначчи: 5
# 1 1 2 3 5

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\8.py"
# Введите натуральное число - кол-во чисел Фибоначчи: 12
# 1 1 2 3 5 8 13 21 34 55 89 144