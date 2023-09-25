'''Срезы списков (сегменты). Работать с конкретными элемнтами списка'''
name = ['asdas', 'ник', 'анна', 'мия', 'аль']
print(name[0:3]) # Выводим сегмент включающий только первые три имени
print(name[1:4])
print(name[:3]) # Если первый индекс элемента не указан то отсчет начинается с начала спсика
print(name[1:])# Если последний индекс элемента не указан то отсчет идет с до конца спсика

print('Переберем первые три имени')
for n in name[:3]:
    print(n.title())

# Копирование списка
name_2 = name[:]
name_2.append('фредерико')

name_3 = name
name_3.append('майя')


print(name)
print(name_2)
print(name_3)