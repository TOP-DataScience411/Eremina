# Написать программу, которая принимает пользовательский ввод только до тех пор пока он соответствует условию
# Программе в цикле получает из стандартного потока ввода (stdin) по одному целому числу, кратному семи. 
# При появлении любого числа, не делящегося на семь, цикл прерывается
# После окончания цикла программа выводит в stdout в одну строку все числа, кратные семи, в обратном порядке
my_list = []
while True:
    chislo = int(input('Введите целое число: '))
    if chislo % 7 != 0:
        break
    else: 
        my_list == my_list.append(chislo)  
print(my_list[::-1])
# ========================================================
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\3.1.py"
# Введите целое число: 21
# Введите целое число: 7
# Введите целое число: 777
# Введите целое число: 69
# [777, 7, 21]

# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\3.1.py"
# Введите целое число: 35
# Введите целое число: 77
# Введите целое число: 14
# Введите целое число: 21
# Введите целое число: 56
# Введите целое число: 777
# Введите целое число: 12
# [777, 56, 21, 14, 77, 35]
