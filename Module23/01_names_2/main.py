numbers_sumbol = 0
line_count = 0

file = open('people.txt', 'r', encoding='utf-8')
for word in file:
    line_count += 1
    lenght = len(word)
    try:
        if word.endswith("\n"):
            lenght -= 1
        if lenght < 3:
            raise BaseException
        numbers_sumbol += lenght
    except BaseException:
        print('Длина {} строки меньше 3 символов'.format(line_count))

file.close()
print('Найденная сумма символовю ', numbers_sumbol)
