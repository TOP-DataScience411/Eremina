# Написать генераторную функцию с именем deck, которая создаёт упорядоченную колоду карт
def desk(): 
    lst = ['черви', 'бубны', 'пики', 'трефы']
    for j in lst:
        for i in range(2, 15):
            yield (i, j)
            
            
funcD = desk()
print(funcD)
# ===================================================
# C:\Users\Dina\GIT_LOK_Eremina>python -i "C:\Users\Dina\GIT_LOK_Eremina\2024.11.24\1.py"
# <generator object desk at 0x000001784D363300>
# >>> funcD.__next__()
# (2, 'черви')
# >>> list(desk())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(desk())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> list(desk())[::12]
# [(2, 'черви'), (14, 'черви'), (13, 'бубны'), (12, 'пики'), (11, 'трефы')]
# >>> funcD.__next__()
# (3, 'черви')
# >>> list(desk())[::13]
# [(2, 'черви'), (2, 'бубны'), (2, 'пики'), (2, 'трефы')]
# >>> funcD.__next__()
# (4, 'черви')
# >>>         

# ВОПРОС: Геннадий, поясните, пжст, синтаксис list(desk())[::13]