import re
from collections import Counter

file = open('text.txt', 'r')
text = ''
for line in file:
    text = text + line

letters = Counter(re.findall('[a-z]', text.lower()))
#Как отсортировать словарь по значениям и по ключам?
for letter in letters:
    with open('analysis.txt', 'a') as file_new:
        file_new.write(letter + ' ')
        number = round((letters[letter] / sum(letters.values())), 3)
        number = str(number)
        file_new.write(number + '\n')
