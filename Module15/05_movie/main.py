films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favourite_films = []
favourite_film = input('Введите фильм: ')
while favourite_film != 'end':
    for film in films:
        if film == favourite_film:
            favourite_films.append(film)
    print('Ошибка, такого фильма нет.')
    favourite_film = input('Введите фильм: ')

print('Список любимых фильмов: ', favorite_films)


