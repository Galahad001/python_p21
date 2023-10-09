# Передача списка
def spis(names):
    for name in names:
        msg = f'Hello {name.title()}'
        print(msg)

usernames = ['Нико', 'олег', 'мия']
spis(usernames)



def print_user(user, user_verefi):
    while user:
        u = user.pop()
        print('Взяли пользователя ', u)
        user_verefi.append(u)

def show_user_verefi(user_verefi):
    print('\nПользователи прошедшие проверку')
    for i in user_verefi:
        print(i)

user = ['Никола', 'Мия', 'Анна']
user_verefi = []

print_user(user, user_verefi)
show_user_verefi(user_verefi)