word = input('Введите слово: ')
word = list(word)
unique_letters = 0

for i_word in word:
    coincidences = 0
    for y_word in word:
        if i_word == y_word:
            coincidences += 1
    if coincidences == 1:
        unique_letters += 1

print('Количество уникальных букв: ', unique_letters)