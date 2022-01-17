line = input('Введите строку: ')

max_word = max(line.split(), key=len)
word = len(max_word)

print('Самое длинное слово: ', max_word)
print('Длина этого слова: ', word)


