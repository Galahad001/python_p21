# Словарь в словаре
users = {
    'Mr.fredo':{
        'name': 'fredo',
        'live_game': 'GTA5',
        'location': 'Москва'
    },

    'Mr.combo':{
        'name': 'combo',
        'live_game': 'Mortal Combat',
        'location': 'Краснодар'
    }
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full = f'\tЛюбит играть в {user_info["live_game"]}. Живет в городе {user_info["location"]}'
    print(full)