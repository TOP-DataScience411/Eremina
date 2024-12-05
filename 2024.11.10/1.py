# Написать функцию с именем strong_password, которая проверяет, является ли пароль надёжным

# str_.islower() если все символы в строке являются буквами нижнего регистра, метод вернёт значение True
# str.isupper() если все символы в строке являются буквами верхнего регистра, метод вернёт значение True
    
def strong_password(str_):
    if str_.islower() == True or str_.isupper() == True:
        return print("False. Исправьте регистр")
    else: # если в строке есть символы и верхнего, и нижнего регистра
        if str_.isalnum() == True:
            return print("False. Нет специальных символов")
        else:    
            if len(str_) < 8:
                return print("False. Неверная длина пароля")
            else: # длина строки более или равна 8 символам, есть символы и верхнего, и нижнего регистра
                kol_cifr = 0
                for i in str_:
                    if i.isdigit() == True:                    # символ - цифра
                        kol_cifr = kol_cifr + 1
                if kol_cifr < 2:
                    return print("False. Мало цифр")
                else:
                    return print("True. Хороший пароль")
text_vvod = str(input('Введите пароль:          '))        
strong_password(text_vvod)            
#=======================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\1.py"
# Введите пароль:          sdfsdfsdfsdfdsf
# False. Исправьте регистр

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\1.py"
# Введите пароль:          sDdsfDfg
# False. Нет специальных символов

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\1.py"
# Введите пароль:          dfDg&dg
# False. Неверная длина пароля

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\1.py"
# Введите пароль:          Dfgd&,ds/m
# False. Мало цифр

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\1.py"
# Введите пароль:          Ffd658&sdlK
# True. Хороший пароль