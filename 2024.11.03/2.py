# Написать программу, которая подсчитывает сумму введённых положительных чисел.
# Программа получает из stdin натуральное число n. Затем получает из stdin по очереди n целых чисел.
# Сумму положительных чисел из введённых программа выводит в stdout.
N = int(input('Введите натуральное число N: '))
sumD = 0
for i in range(1, N+1):
    chislo = int(input('Введите целое число: '))
    if chislo > 0:
        sumD = sumD + chislo
print('Суммa всех положительных чисел из введённых= ', sum)
# ========================================================
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\3.2.py"
# Введите натуральное число N: 5
# Введите целое число: 5
# Введите целое число: 15
# Введите целое число: -4
# Введите целое число: 20
# Введите целое число: 10
# Суммa всех положительных чисел из введённых=  50
#
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\3.2.py"
# Введите натуральное число N: -4
# Суммa всех положительных чисел из введённых=  0
#
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\3.2.py"
# Введите натуральное число N: 5
# Введите целое число: -4
# Введите целое число: -3
# Введите целое число: -1
# Введите целое число: -4
# Введите целое число: 5
# Суммa всех положительных чисел из введённых= 5
