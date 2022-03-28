result = 0

with open('calc.txt', 'r') as file:
    for line in file:
        try:
            result += eval(line)
        except:
            if input('Обнаружена ошибка:' + line + 'Хотите исправить?') == 'да':
                line = input('Введите исправленную строку:')
                result += eval(line)

print(result)
