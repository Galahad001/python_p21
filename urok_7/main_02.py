# Возвращаемое значение
# Команда return передает значение из функции в точку программы, в которой эта функция была вызвана

def get_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

res = get_name('Илон', 'Маск')
print(res)



# Возвращение словаря
def user(first_name, last_name, age=None):
    person = {'first': first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

slov = user('Монти', 'Пайтон')
print(slov)
slov2 = user('Монти', 'Пайтон', 100)
print(slov2)



# ИСпользование функ. в цикле while
def get_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name

while True:
    print("Введите Ваше имя ")
    print('Введите q для выхода ')
    f_name = input('Имя ')
    if f_name == 'q':
        break

    l_name = input('Фамилия ')
    if l_name == 'q':
        break

    form_name = get_name(f_name, l_name)
    print('Привет', form_name)