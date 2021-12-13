number_N = int(input('Введите длину списка: '))

number_list = [1 if i % 2 == 0 else i % 5 for i in range(number_N)]

print('Результат:', number_list)
