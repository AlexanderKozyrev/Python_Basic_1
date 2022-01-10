text = input('Введите текст: ')
vowel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
vowel_letters_text = []

# TODO правим нейминг переменных
for i in range(len(text)):
    for j in range(len(vowel_letters)):
        if vowel_letters[j] == text[i]:
            vowel_letters_text.append(text[i])

print('Список гласных букв: ', vowel_letters_text)
# TODO фукнции не вызываем внутри других функций
print('Длина списка: ', len(vowel_letters_text))

