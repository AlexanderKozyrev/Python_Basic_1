number_max = int(input('Введите максимальное число: '))
numbers_set = set(range(1, number_max + 1))

while True:
    numbers = input('Нужное число есть среди вот этих чисел: ')
    if numbers == 'Помогите':
        print('Артем мог загадать следующие числа: ', numbers_set)
        break
    else:
        new_numbers_set = set(map(int, numbers.split()))

    if input('Ответ Артема: ') == 'Да':
        numbers_set &= new_numbers_set
    else:
        numbers_set -= new_numbers_set
