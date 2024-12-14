import shutil
terminal_size = shutil.get_terminal_size()           #для себя: print(f"Колонки: {terminal_size.columns}, строки {terminal_size.lines}")
#=============================================================================================
def dlin_stroka(str_nach: str) -> list:
    ''' функция работает с длинной строкой - нарезает ее на отрезки строк приемлемой длины '''
    lst = str_nach.split()
    for i in range(0,len(lst)):
        if i == 0:
            str_obr = lst[i]
        else:
            if len(str_obr + ' ' + lst[i]) < (terminal_size.columns - 5):
                str_obr = str_obr + ' ' + lst[i]
            else:
                str_obr = str_obr
    str_nach_obr = str_nach.replace(str_obr,"")
    return [str_obr, str_nach_obr]  # обрезанная начальная строка и "обрезок"
#=============================================================================================
def important_message(str_) -> str:
    lst_obr = []
    for i in range(0, len(str_) // (terminal_size.columns - 5) + 1): #создаем список из обрезанных строк
        if i==0:
            lst_obr.insert(i, dlin_stroka(str_)[0])
            str_1 = dlin_stroka(str_)[1] #длинный остаток
        else:
            lst_obr.insert(i, dlin_stroka(str_1)[0])
            str_1 = dlin_stroka(str_1)[1]  #длинный остаток
# результат - создан список lst_obr, где элементы - нарезки строк нужной длины, str_1 на "выходе" - пустая

# далее - решаем задачу - чертим рамку вокруг текста
    print('#', '=' * (terminal_size.columns - 1), '#', sep = '') #79 знаков "="
    print('#', ' ' * (terminal_size.columns - 1), '#', sep = '')

    for i in range(0, len(str_) // (terminal_size.columns - 5) + 1):
        print('# ',lst_obr[i].center(terminal_size.columns - 5,' '),' #')
    
    print('#', ' ' * (terminal_size.columns - 1), '#', sep = '')
    print('#', '=' * (terminal_size.columns - 1), '#', sep = '')
