# Начинаем с двух списков: пользователей для проверки и пустого списка для хранения проверенных пользователей
unconfirmed_users = ['анна', 'олег', 'мия']
confirmed_users = []

# Проверяем каждого пользователя, пока омтаются непроверенные пользователию Каждый пользователь, прошедший проверку, перемещается в список проверенных
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f'Проверка пользователя: {current_user.title()}')
    confirmed_users.append(current_user)

# Вывод всех проверенных пользователей
print('\t\n Проверенны следующие пользователи:')
for user in confirmed_users:
    print('\t', '- ', user.title())



# Удаление всех вхождений конкретного значения из списка
cars = ['киа','хендай','киа','киа','шевроле']
print(cars)

while 'киа' in cars:
    cars.remove('киа')

print(cars)


# Заполнение словаря данными, введенными пользователем
responses = {}

# Усьановка флага 
active = True

while active:
    # Запрос имени и ответа пользователя
    name = input('Ваше имя ')
    response = input('Что Вы думаете о языке программирования Python? ')

    # Сохраняем в словарь
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input('Хотите продолжить опрос (да/нет) ')
    if repeat == 'нет':
        active = False

# Вывод результатов опроса
print('----- Результаты -----')
for name, response in responses.items():
    print(f"{name} думает о языке программирования Python следующее: {response}")
