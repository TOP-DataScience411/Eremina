# Написать функцию с именем taxi_cost, которая вычисляет стоимость поездки на такси
def taxi_cost(rasst: int, time_ogid: int = 0) -> int | None: 
    if rasst < 0 or time_ogid < 0:
        return None
    else:
        if rasst == 0:
           return(print(round(80 + 80 + time_ogid * 3)))
        else:
           return(print(round(80 + (rasst / 150) * 6 + time_ogid * 3)))
#========================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python -i "C:\Users\Dina\GIT_LOK_Eremina\2024.11.10\2.py"
# >>>
# >>> taxi_cost(42130, 8)
# 1789
# >>> taxi_cost(1500)
# 140
# >>> taxi_cost(2560)
# 182
# >>> taxi_cost(0, 5)
# 175
# >>> print(taxi_cost(-300))
# None
# >>>