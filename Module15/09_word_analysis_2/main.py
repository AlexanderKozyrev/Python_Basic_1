word = input('Введите слово: ')
word = list(word)
opposite_word = []
index = 1

for _ in range(len(word)):
    opposite_word.append(word[-index])
    index += 1

if word == opposite_word:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом')

# зачет!
