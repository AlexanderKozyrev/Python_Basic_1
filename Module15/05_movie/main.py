films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourite_films = []
film = input('Введите фильм: ')

while film != 'end':
    if film in films:
        favourite_films.append(film)
    else:
        print('Ошибка, такого фильма нет')
    film = input('Введите фильм: ')

print('Список любимых фильмов: ', favourite_films)
