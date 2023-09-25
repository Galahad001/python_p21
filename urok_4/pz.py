'''Написать цепочку if-elif-else для определения периода жизни человека. Создать переменную. Вывести сообщение'''
'''Если значение меньше 2 - младенец
    Больше либо равно 2, но меньше 4 - малыш
    Больше либо равно 4, но меньше 13 - ребенок
    Больше либо равно 13, но меньше 20 - подросток
    Больше либо равно 20, но меньше 65 - Взрослый
    Больше либо равно 65 - пожилой
    '''

age = 66
if age < 2:
    print('Ребенок')
elif age >= 2 and age < 4:
    print('Малыш')
elif age >= 4 and age < 13:
    print('Ребенок')
elif age >= 13 and age < 20:
    print('Подросток')
elif age >= 20 and age < 65:
    print('Взрослый')
else:
    print('Пожилой')