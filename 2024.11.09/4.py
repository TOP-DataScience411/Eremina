# Написать программу, которая проверяет, является ли один список частью другого списка
print('Ввeдите парами число и строку, разделенные пробелом; конец ввода - пустая строка ')
str1 = ""
while True:
    user_input = input()
    if user_input == '':
        break
    else:
        str1 = str(str1 + user_input + ",")
# -----------------------------------конец ввода данных----------------------------------------------
str1 = str1[:-1] # убираю лишнюю запятую
dict1 = {}
for pair in str1.split(","):
    key, value = pair.split(" ")
    dict1[key] = value
text_vvod = str(input('Введите одно из введенных ранее значений:          '))
key_print = 0
for key, value in dict1.items():
    if value == text_vvod:
        key1 = key
        key_print = key_print + 1
        break
if key_print == 0:
    print("! value error !")
else:
    print(key1)
# =================================================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\4.py"
# Ввeдите парами число и строку, разделенные пробелом; конец ввода - пустая строка
# 1 раз
# 2 два
# 3 три

# Введите одно из введенных ранее значений:          три
# 3

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\4.py"
# Ввeдите парами число и строку, разделенные пробелом; конец ввода - пустая строка
# 1 раз
# 2 два
# 3 три
# 4 четыре

# Введите одно из введенных ранее значений:          пять
# ! value error !