# Написать функцию с именем schedule, которая генерирует график проведения мероприятий по заданным условиям
# 1 - пн, 2 - вт, 3 - ср, 4 - чт, 5 - пт, 6 - сб, 7 - вс
#================??????????????????????????=============
# vacations = [strptime(date(2024, 5, 1), timedelta(weeks=1)),strptime(date(2024, 7, 17), timedelta(weeks=1))]
# !!! использовать данную конструкцию в таком виле не получилось: на выходе получается такой список 
# vacations= [(datetime.date(2024, 5, 1), #datetime.timedelta(days=7)), (datetime.date(2024, 7, 17), datetime.timedelta(days=7))], # вместо списка дат
# победить это не удалось, буду благодарна за обратную связь - как это можно сделать
# также не удалось разобраться - как обратиться к переменной, которая создавалась как *args (произвольный набор). Набор может быть 
# длинным, а как обратиться к отдельному элементу этого набора, когда его вызываешь (при уточнении дня недели, например) 
# нужна Ваша подсказка
#================??????????????????????????=============
import datetime
from datetime import date, timedelta
                          # timedelta возвращает объект продолжительности, который можно сложить с объектом datetime и получить новую дату
# vacations: list[tuple[datetime.date, datetime.timedelta]] - вместо этого просто "ручной" список
vacations = ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-04', '2024-05-05', '2024-05-06', '2024-05-07','2024-06-17', '2024-06-18','2024-06-19', '2024-06-20', '2024-06-21', '2024-06-22', '2024-06-23']
def schedule(date_first: datetime.date, day_week: int, /, *args: int, total_days: int, format_date = '%d/%m/%Y') -> list: 
#    print(f"date_first= {date_first}, day_week= {day_week}, *args= {args}, total_days= {total_days} format_date = {format_date}")
    lst = []
    for i in range(total_days):
        lst.append(str(date_first + timedelta(i)))
    lst2 = [item for item in lst if item not in vacations]
    return lst2
def weekday(date_str):
    return datetime.strptime(date_str).weekday()
py321 = schedule(date(2024,5,1), 6, 7, total_days = 70)
#result = [[date for date in py321 if weekday(date) == n] for n in {6, 7}]
print('len(py321)= ', len(py321))
print('py321[36:46]= ', py321[36:46])
#print('result=', result)
#====================================================================================
# почистить список от vacations в упрощенном  виде удалось, но с днями недели - проблема, нужна помощь
# не поняла до конца как передавать туда-сюда переменные, например, как правильно передать day_week?
# result не срабатывает, что не так?
#====================================================================================
# C:\Users\Dina\GIT_LOK_Eremina>python "C:\Users\Dina\GIT_LOK_Eremina\2024.12.01\1.py"
# len(py321)=  56
# py321[36:46]=  ['2024-06-13', '2024-06-14', '2024-06-15', '2024-06-16', '2024-06-24', '2024-06-25', '2024-06-26', '2024-06-27', '2024-06-28', '2024-06-29']
 

 

