numbers_words = int(input('Введите количество пар слов: '))
words_dict = {}

for number in range(numbers_words):
    couple = input(f'{number + 1} пара: ').lower().split(' - ')
    words_dict[couple[0]] = couple[1]

print(words_dict)
while True:
    word = input('Введите слово: ').lower()
    if word in words_dict:
        print('Синоним: ', words_dict[word])
    elif word in words_dict.values():
        print('Синоним: ', words_dict.values(word))
    else:
        print('Такого слова в словаре нет.')

