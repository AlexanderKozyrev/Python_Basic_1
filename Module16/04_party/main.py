guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print('Сейчас на вечеринке', len(guests), 'человек:', guests)
    action = input('Гость пришел или ушел? ')
    if action == 'пришел':
        name = input('Введите имя гостя: ')
        print('Привет, ', name)
        if len(guests) == 6:
            print('Прости ', name, 'но мест нет')
        else:
            guests.append(name)

    if action == 'ушел':
        name = input('Введите имя гостя: ')
        print('Пока, ', name)
        guests.remove(name)

    if action == 'Пора спать':
        print('Вечеринка закончилась, пора спать.')
        break
    print()

