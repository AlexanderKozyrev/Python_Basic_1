alpha = []
for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    alpha.append(i)

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
s = ''
for i in text:
    if i == ' ':
        s = s + ' '
    else:
        k = alpha.index(i) + shift
        if k > 32:
            k = k - 33
        s = s + alpha[k]

print('Зашифрованное сообщение: ', s)

# TODO применить рекомендации данные ранее
