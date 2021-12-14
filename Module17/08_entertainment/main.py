stick = int(input('Количество палок: '))
sticks = ['I' for _ in range(stick)]

throws = int(input('Количество бросков: '))
for i in range(1, throws + 1):
    throw_from = int(input(f'Бросок {i}, Сбиты палки с номера '))
    throws_to = int(input('по номер '))
    for j in range(throw_from - 1, throws_to):
        sticks[j] = '.'

print('Результат: ', end='')
for i in range(stick):
    print(sticks[i], end='')

