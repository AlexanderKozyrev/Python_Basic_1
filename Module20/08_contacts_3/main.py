
phone_book = {'Петров Ваня': 8954556, 'Петров Леня': 8954556}

while True:
    action = int(input('\nВведите номер действия: \n1. Добавить контакт \n2. Найти человека \n'))
    if action == 1:
        name = input('Введите Имя и Фамилию контакта: ')
        telephone = input('Введите номер телефона: ')
        if name in phone_book:
            print('Такой человек уже есть в словаре!')
        else:
            phone_book[name] = telephone
        print(phone_book)
    else:
        surname = input('Введите фамилию: ').lower()
        for names, number in phone_book.items():
            if surname in names.lower():
                print(names, number)