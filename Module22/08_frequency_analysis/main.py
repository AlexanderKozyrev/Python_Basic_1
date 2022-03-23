import re
from collections import Counter

file = open('text.txt', 'r')
text = ''
for line in file:
    text = text + line

letters = Counter(re.findall('[a-z]', text.lower()))
#Как отсортировать словарь по значениям и по ключам?
for letter in letters:
    print(f'{letter} {letters[letter] / sum(letters.values()):.3f}')