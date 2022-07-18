import re


numbers_telefon = ['9999999999', '999999-999', '99999x9999']
number_pattern = r'\b[8-9]\d{9}'

for number in range(len(numbers_telefon)):
    if re.findall(number_pattern, numbers_telefon[number]):
        print(number + 1, 'номер: все в порядке')
    else:
        print(number + 1, 'номер: не подходит')

