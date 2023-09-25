'''Простая команда if'''
age = 19 
if age >= 18:
    print('Вам можно посещять данный сайт')
    print('Добро пожаловать')


'''Команда else исполнится в любом случае. Если предыдущие проверки не прошли условие'''
age_1 = 17
if age >= 18:
    print('Вам можно посещять данный сайт')
    print('Добро пожаловать')
else:
    print('Вам меньше 18')
    print('Вход на сайт запрещен')


'''if-elif-else'''
'''Для проверки более двух возможных вариантов. Существует синтаксис if-elif-else. Все условия выполняются по 
порядку, пока одно из них не даст истинный результат.'''
age_2 = 15
if age_2 < 4:
    print('Проезд бесплатный')
    # price = 0
elif age_2 < 18:
    print('Проезд 36 руб')
    # price = 36
else:
    print('Проезд 40 руб')

# print(f'Проезд {price}')


print('--------')
'''Серии блоков elif'''
age_3 = 15

if age_3 < 4:
    price = 0
elif age_3 < 18:
    price = 36
elif age_3 < 40:
    price = 40
else:
    price = 20
print(f'Проезд будет равен {price} руб')


print('----------')
'''Проверка нескольких условий'''
pizzas = ['пеперони', 'мясная', '3 сыра']

if 'пеперони' in pizzas:
    print(pizzas[0].title())
if 'мясная' in pizzas:
    print(pizzas[1].title())
if '3 сыра' in pizzas:
    print(pizzas[2].title())

print('-------')

if 'пеперони' in pizzas:
    print(pizzas[0].title())
elif 'мясная' in pizzas:
    print(pizzas[1].title())
else:
    print(pizzas[2].title())