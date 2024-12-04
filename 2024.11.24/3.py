# Написать рекурсивную функцию с именем tree_leaves, которая считает количество листьев на дереве.
# Функция принимает обязательным позиционно-ключевым аргументом список веток дерева

tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
#--------------------------------------------------------------
def tree_leaves(lst_): # делаем многоуровневый список линейным
    if not lst_:
        return lst_
    if type(lst_[0]) is list:
        return tree_leaves(lst_[0]) + tree_leaves(lst_[1:])
    return lst_[:1] + tree_leaves(lst_[1:])
#-------------------------------------------------------------- получен линейный список "листов дерева", их просто нудно посчитать

print(len(tree_leaves(tree)))
#======================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python -i C:\Users\Dina\GIT_LOK_Eremina\2024.11.24\3.py
# 38
# >>> len(tree_leaves(tree))
# 38
# >>> tree_leaves(tree)
# ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf']
# >>>