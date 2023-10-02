# Перебор слоаря
# Словарь может содержать огромное количество пар ключ-значение

user = {
    'name': 'fredo',
    'nickname': 'Mr.fredo',
    'point': 100,
}

# Чтобы написать цикл для словаря надо создать две переменные. В них хранится клюс и значение из каждой пары.
# Имя словаря за которым следует вызов метода items(), возвращает список пар ключ значение.
for key, value in user.items():
    print(f'Key: {key}')
    print(f'Value: {value} \n')



# Перебор всех ключей в словаре
'''Метод keys() - удобен, если не нужно работать мо значениями словаря'''
stran = {
    'давид': 'москва',
    'николь': 'краснодар',
    'мия': 'анапа',
    'ник': 'владивосток',
    'анна': 'владивосток',
}

# stran.keys() - извлекаетт из словаря только ключи
for name in stran.keys():
    print(name.title())

print()

names = ['давид', 'ник']
for name  in stran.keys():
    print(name.title())

    if name in names:
        res = stran[name].title()
        print(f'\t{name.title()}, ты из города {res}')

# Перебор ключей в определенном порядке
for name in sorted(stran.keys()):
    print(name)

print()

# Переебор всех значений словаря.
for val in stran.values():
    print(val)

print()

# Если в словаре повторяется значение можно использовать set() - получить список значений без повторений.
for city in set(stran.values()):
    print(city)