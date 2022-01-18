text = input('Введите строку: ')
counter = 1
print(len(text))
for letter in range(len(text) - 1):
    if text[letter] == text[letter + 1]:
        counter += 1
    else:
        print(text[letter], end='')
        print(counter, end='')
        counter = 1

print(text[len(text) - 1], end='')
print(counter, end='')

