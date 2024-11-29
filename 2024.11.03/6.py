# Написать программу, которая проверяет транспортный билет
n = int(input('Введите шесть цифр - номер билета: '))
list_n = [int(i) for i in str(n)]
if list_n[0] + list_n[1] + list_n[2] == list_n[3] + list_n[4] + list_n[5]:
    print("да")
else:
    print("нет")
# ========================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\6.py"
# Введите шесть цифр - номер билета: 183534
# да

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\6.py"
# Введите шесть цифр - номер билета: 401367
# нет

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\6.py"
# Введите шесть цифр - номер билета: 111222
# нет

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.03\6.py"
# Введите шесть цифр - номер билета: 554455
# да