﻿#Напишите программу, которая бы при запуске случайным образом отображала
#имя одного из двенадцати апостолов.



import random
 
print ("Программа случайным образом отображает имя одного из двенадцати апостолов.")
 
 x = int (random.randint(1,4))
 
 print ('\nОдин из основателей - ', end = '')
 
 if x == 1:
     print ('Иуда.')
 elif x == 2:
     print ('Пётр.')
 elif x == 3:
     print ('Иоанн.')
elif x == 4:
     print ('Иаков Зеведеев.')
elif x == 5:
     print ('Филипп.')
elif x == 6:
     print ('Варфоломей.')
elif x == 7:
     print ('Матфей.')
elif x == 8:
     print ('Фома.')
elif x == 9:
     print ('Иаков Алфеев.')
elif x == 10:
     print ('Фаддей.')
elif x == 11:
     print ('Симон Канани.')
 else:
     print ('Андрей.')

     
 input("\nДля выхода нажмите Enter.") 