numbers_words = int(input('Введите количество пар слов: '))
words_dictionary = {}

for number in range(numbers_words):
    couple = input(f'{number + 1} пара: ').lower().split(' - ')
    words_dictionary[couple[0]] = couple[1]

print(words_dictionary)
while True:
    word = input('Введите слово: ').lower()
    if word in words_dictionary:
        print('Синоним: ', words_dictionary[word])
    elif word in words_dictionary.values():
        print('Синоним: ', words_dictionary.values(word))
    else:
        print('Такого слова в словаре нет.')


