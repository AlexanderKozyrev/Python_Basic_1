menu = input('Доступное меню: ')

available_menu = menu.split(';')
application_menu = ', '.join(available_menu)

print('На данный момент в меню есть: ', application_menu)