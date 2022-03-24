zen_file = open('zen.txt', 'r')
number_line = 0
number_word = 0
number_letter = 0

for line in zen_file:
    number_line += 1
    number_word += len(line.split())
    number_letter += sum(map(str.isalpha, line))

print('Количество строк в файле: ', number_line)
print('Количество слов в файле: ', number_word)
print('Количество букв в файле: ', number_letter)

