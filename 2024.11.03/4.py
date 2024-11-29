# Написать программу, которая подсчитывает количество простых чисел среди всех чисел одной разрядности
n = int(input('Введите натуральное число - кол-во разрядов: '))
p_nach = 10 ** (n - 1)  # определяем первое число при данной разрядности
p_kon = 9 * 10 ** (n - 1)   # определяем количество чисел данной разрядности
kol_all = 0
for chislo in range(p_nach, p_nach + p_kon):  # цикл по всем числам заданной разрядности от первого до последнего
    kolD = 0
    for i in range(1, chislo+1):
        if chislo % i == 0:
            kolD = kolD + 1
    if kolD == 2:
        kol_all = kol_all + 1
print(kol_all)
#========================================================
# C:\Users\Dina\GIT_LOK_Eremina>python C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\4.py
# Введите натуральное число - кол-во разрядов: 1
# 4

# C:\Users\Dina\GIT_LOK_Eremina>python C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\4.py
# Введите натуральное число - кол-во разрядов: 2
# 21

# C:\Users\Dina\GIT_LOK_Eremina>python C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\4.py
# Введите натуральное число - кол-во разрядов: 3
# 143

# C:\Users\Dina\GIT_LOK_Eremina>python C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\4.py
# Введите натуральное число - кол-во разрядов: 4
# 1061