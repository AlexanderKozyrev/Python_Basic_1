fail = input('Введите название файла: ')
symbol = '@№$%^&*()'

fail_s = fail.split('.')

if fail_s[1] != 'txt' and fail_s[1] != 'docx':
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
# TODO тут тогда нужно добавить fail[0][0]
elif fail[0] in symbol:
    print('Ошибка: название начинается на один из специальных символов')
else:
    print('Файл назван верно.')
