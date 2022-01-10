text = input('Введите текст: ')
vowel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
vowel_letters_text = []

for index in range(len(text)):
    for number in range(len(vowel_letters)):
        if vowel_letters[number] == text[index]:
            vowel_letters_text.append(text[index])

print('Список гласных букв: ', vowel_letters_text)
text_length = len(vowel_letters_text)
print('Длина списка: ', text_length)

