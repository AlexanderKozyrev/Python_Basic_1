alphabet = []
for letter in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
    alphabet.append(letter)

text = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))
new_text = ''
for sign in text:
    if sign == ' ':
        new_text = new_text + ' '
    else:
        letter_number = alphabet.index(i) + shift
        if letter_number > 32:
            letter_number = letter_number - 33
        new_text = new_text + alphabet[letter_number]

print('Зашифрованное сообщение: ', new_text)

