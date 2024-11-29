# Написать программу, которая проверяет корректность введённого адреса электронной почты
text_vvod = str(input('Введите текст:          '))
if text_vvod.count("@") == 1:
    if text_vvod.count(".") == 1:
        n1 = text_vvod.index("@")
        n2 = text_vvod.index(".")
        if n1 + 1 < n2 and n1 != 0 and n2 != 0 and n1 != len(text_vvod) - 1  and n2 != len(text_vvod) - 1:
            print("да")
        else:
            print("нет")
    else:
        print("нет")
else:
    print("нет")
#==================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\1.py"
# Введите текст:          dindin1414@mail.ru
# да

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\1.py"
# Введите текст:          dindin1414@mail.
# нет

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\1.py"
# Введите текст:          @dindin1414@mail.
# нет

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\1.py"
# Введите текст:          dind@in1414@mail.ru
нет