# Написать программу, которая проверяет корректность хода шахматного короля
# ========================================================
bukvas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] # определение корректного списка буквенных обозначений шахматных клеток
chiclos = range(1, 9) # определение корректного перечня цифровых обозначений шахматных клеток
#
bukva1 = input('Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение первой ячейки:').lower()
if bukva1 not in bukvas:
    print('Введена неправильная буква, используйте указанный список a-h')
else:
        chiclo1 = int(input('Введите число от 1 до 8  =>>> цифровое обозначение первой ячейки:'))
        if chiclo1 not in chiclos:
            print('Введено неправильное число, используйте только 1-8')
        else:
            bukva2 = input('Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение второй ячейки:').lower()
            if bukva2 not in bukvas:
                print('Введена неправильная буква, используйте указанный список a-h')
            else:
                    chiclo2 = int(input('Введите число от 1 до 8  =>>> цифровое обозначение второй ячейки:'))
                    if chiclo2 not in chiclos:
                        print('Введено неправильное число, используйте только 1-8')
                    else:
                        if bukva1 == 'a':
                            x1 = 1
                        if bukva1 == 'b':
                            x1  =2
                        if bukva1 == 'c':
                            x1 = 3
                        if bukva1 == 'd':
                            x1 = 4
                        if bukva1 == 'e':
                            x1 = 5                            
                        if bukva1 == 'f':
                            x1 = 6
                        if bukva1 == 'g':
                            x1 = 7
                        if bukva1 == 'h':
                            x1 = 8    
                        if bukva2 == 'a':
                            x2 = 1
                        if bukva2 == 'b':
                            x2 = 2
                        if bukva2 == 'c':
                            x2 = 3
                        if bukva2 == 'd':
                            x2 = 4
                        if bukva2 == 'e':
                            x2 = 5                            
                        if bukva2 == 'f':
                            x2 = 6
                        if bukva2 == 'g':
                            x2 = 7
                        if bukva2 == 'h':
                            x2 = 8                                
                        #получились числовые адреса(x1,chiclo1) и (x2, chiclo2)
                        if (x1 == x2+1 or x1 == x2-1 or x1 == x2) and (chiclo1 == chiclo2 + 1 or chiclo1 == chiclo2 - 1 or chiclo1 == chiclo2):
                            print('да')
                        else:
                            print('нет')
# ========================================================
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\2.6.py"
# Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение первой ячейки:f
# Введите число от 1 до 8  =>>> цифровое обозначение первой ячейки:2
# Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение второй ячейки:g
# Введите число от 1 до 8  =>>> цифровое обозначение второй ячейки:3
# да
# 
# C:\Users\Dina>python "D:\!   ___ОБУЧЕНИЕ DS\_ЗАДАНИЯ_DS\2.6.py"
# Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение первой ячейки:f
# Введите число от 1 до 8  =>>> цифровое обозначение первой ячейки:3
# Введите английскую букву из списка a b c d e f g h  =>>> буквенное обозначение второй ячейки:f
# Введите число от 1 до 8  =>>> цифровое обозначение второй ячейки:5
# нет
