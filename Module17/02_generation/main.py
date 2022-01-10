number_N = int(input('Введите длину списка: '))

numbers_new = [1 if number % 2 == 0 else number % 5 for i in range(number_N)]

print('Результат:', numbers_new)
