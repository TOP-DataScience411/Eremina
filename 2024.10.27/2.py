# ИСПОЛЬЗОВАТЬ везде: в большинстве случаев PEP 8 рекомендует добавлять пробелы вокруг бинарных операторов (исключения: оператор возведения в степень, операторы умножения и деления в длинных выражениях)
chislo = int(input('Введите целое число: '))
# chislo_sled = int(chislo) + 1 - старый вариант
# ИСПРАВИТЬ: повторное вычисление одного и того же объекта неоптимально
# chislo_pred = int(chislo) - 1 - старый вариант
#chislo_pred = int(chislo) - 1 - старый вариант
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (не хватает пробела)
# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробел между передаваемыми в функцию аргументами
print("Следующее за числом ", chislo, " число: ", chislo+1, "\nДля числа ", chislo, " предыдущее число: ", chislo-1, sep='') # поправлено
# ИСПОЛЬЗОВАТЬ: '\nabc' вместо '\n', 'abc'
#=======================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.10.27\2.py"
# Введите целое число: 20
# Следующее за числом 20 число: 21
# Для числа 20 предыдущее число: 19

# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/


# ИТОГ: доработать — 2/3

