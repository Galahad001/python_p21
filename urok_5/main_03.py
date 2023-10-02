# Вложения - иногда множество словарей надо сохранить в списке или сохранить список как значение словаря.
# Создадим спсиок из пользователей, где каждый элемент это словарь с информацией о пользователе.
user_0 = {'name': 'nick', 'age':25}
user_1 = {'name': 'anna', 'age':18}
user_2 = {'name': 'gregory', 'age':30}

users = [user_0, user_1, user_2]
# Занесли всех пользователей в спсиок
for user in users:
    print(user)


print('--------------------')

cars = []

for car in range(30):
    new_cars = {'color': 'red', 'dors': 5, 'price':10000}
    cars.append(new_cars)

for car in cars[0:3]:
    if car['color'] == 'red':
        car['color'] = 'blue'
        car['dors'] = 3 
        car['price'] = 15000


for car in cars[:5]:
    print(car)

print(len(cars))