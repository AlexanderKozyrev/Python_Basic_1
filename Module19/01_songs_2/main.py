violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

numbers_songs = int(input('Сколько песен выбрать? '))
songs_time = 0

for song in range(numbers_songs):
    name_song = input(f'Название {song + 1} песни: ')
    songs_time += violator_songs[name_song]

# TODO функции из принтов выносим
print('Общее время звучания песен: ', round(songs_time, 2), 'минут')
