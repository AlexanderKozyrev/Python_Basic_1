stick = int(input('Количество палок: '))
sticks = ['I' for _ in range(stick)]

throws = int(input('Количество бросков: '))
for number in range(1, throws + 1):
    throw_from = int(input(f'Бросок {number}, Сбиты палки с номера '))
    throws_to = int(input('по номер '))
    for throw in range(throw_from - 1, throws_to):
        sticks[throw] = '.'

print('Результат: ', end='')
for number in range(stick):
    print(sticks[number], end='')

