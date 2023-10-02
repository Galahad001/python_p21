# Команда break - прерывает цикл независимо от состояния условия

while True:
    city = input('Введите город или "выход" для завершения программы ')

    if city.lower() == 'выход':
        break
    else:
        print(f'Вы ввели город {city.title()}')


# Команда continue - не прерывает цикл, а возвращается к началу циклв и проверки условия.
nums = 0
while nums < 10:
    nums += 1
    if nums % 2 == 0:
        continue

    print(nums)

# Команда continue - игнорирует то что идет после нее и возвращается в начало.