password = input('Придумайте пароль: ')

if len(password) < 8:
    print('Пароль ненадёжный. Попробуйте ещё раз.')
elif sum(map(str.isupper, password)) == 0:
    print('Пароль ненадёжный. Попробуйте ещё раз.')
elif sum(map(str.isdigit, password)) < 3:
    print('Пароль ненадёжный. Попробуйте ещё раз.')
else:
    print('Это надёжный пароль!')