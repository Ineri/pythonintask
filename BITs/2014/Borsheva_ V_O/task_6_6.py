#Задача 6. Вариант 6
#компьютер загадывает название одного из семи городов России, имеющих действующий метрополитен, а игрок должен его угадать.

#Борщёва В.О
#21.03.2016

import random
subways=('Москва','Санкт-Петербург','Нижний Новгород','Новосибирск','Самара','Екатеринбург','Казань')
subway=random.randint(0,6)
rand=subways[subway]
print('я загадал один город,имеющий дейстующий метрополитен')
#print(rand)
otvet=0
while (otvet)!=(rand):
    otvet=input("Введите один из городов:")
    if(otvet)!=(rand):
        print("Вы не угадали. Попробуйте снова.")
    elif (otvet)==(rand):
        print("Вы угадали.")
        break
input(" Нажмите Enter для выхода")        
    
