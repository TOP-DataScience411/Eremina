# Написать программу, которая генерирует форматированную строку
print('Вводите название фруктов последовательно, после каждого нажмите Enter, завершение ввода - повторное Enter ')
lst = []
while True:
    user_input = input()
    if user_input == '':
        break
    else:
        lst.append(user_input)
n = len(lst)
str_itog = ""
if n < 3:
    if n == 1:
        print(str(lst[0]))
    else: # т.е. n=2
        print(str(lst[0] + " и " + lst[1]))
else: # т.е. n>=3
    for i in range(0, n - 2):
        str_itog = str_itog + str(lst[i] + ", ")
    str_itog = str_itog + str(lst[n-2] + " и " + lst[n-1])        
    print(str_itog)
#============================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\2.py"
# Вводите название фруктов последовательно, после каждого нажмите Enter, завершение ввода - повторное Enter
# яблоко

# яблоко

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\2.py"
# Вводите название фруктов последовательно, после каждого нажмите Enter, завершение ввода - повторное Enter
# яблоко
# груша

# яблоко и груша

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\2.py"
# Вводите название фруктов последовательно, после каждого нажмите Enter, завершение ввода - повторное Enter
# яблоко
# груша
# апельсин

# яблоко, груша и апельсин

# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.11.09\2.py"
# Вводите название фруктов последовательно, после каждого нажмите Enter, завершение ввода - повторное Enter
# яблоко
# груша
# апельсин
# лимон

# яблоко, груша, апельсин и лимон
    