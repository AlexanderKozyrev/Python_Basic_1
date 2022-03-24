numbers_sumbol = 0
line_count = 0

file = open('people.txt', 'r', encoding='utf-8')
for word in file:
    line_count += 1
    lenght = len(word)
    if word.endswith("\n"):
        lenght -= 1
    if lenght < 3:
        raise BaseException('Длина {} строки меньше 3 символов'.format(line_count))
    numbers_sumbol += lenght

file.close()
print('Найденная сумма символовю ', numbers_sumbol)
