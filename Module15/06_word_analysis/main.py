word = input('Введите слово: ')
word = list(word)
unique_letters = 0

for i in word:
    coincidences = 0
    for y in word:
        if i == y:
            coincidences += 1
    if coincidences == 1:
        unique_letters += 1

print('Количество уникальных букв: ', unique_letters)


