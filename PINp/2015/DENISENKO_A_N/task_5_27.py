# Задача 5. Вариант 27.
# Напишите программу, которая бы при запуске случайным образом отображала
# название одного из двенадцати месяцев.

# Denisenko A. N.
# 02.06.2016

import random

month = ("Январь", "Февраль","Март", "Апрель",
         "Май", "Июнь","Июль", "Август",
         "Сентябрь", "Октябрь","Ноябрь", "Декабрь")
randmonth = random.choice(month)
print(randmonth)
input("\n\nВведите ENTER для выхода")
