number_N = int(input('Введите длину списка: '))

# TODO работаем над неймингом
number_list = [1 if i % 2 == 0 else i % 5 for i in range(number_N)]

# TODO list set dict tuple не используем в именовании переменных
print('Результат:', number_list)
