chislo=input('Введите положительное трёхзначное число: ')
chislo_int=int(chislo)
sotni=chislo_int//100
desyatki=(chislo_int-sotni*100)//10
edinic=chislo_int-sotni*100-desyatki*10
# ПЕРЕИМЕНОВАТЬ: sum — это имя встроенной функции, объявляя собственную переменную с таким именем вы теряете прямой доступ к встроенной функции
sum=sotni+desyatki+edinic
proizv=sotni*desyatki*edinic
print("Сумма цифр = ",sum,"\n","Произведение цифр = ",proizv,sep='')


# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\Задание 1\4.py"
# Введите положительное трёхзначное число: 333
# Сумма цифр = 9
# Произведение цифр = 27


# ИТОГ: хорошо — 3/4

