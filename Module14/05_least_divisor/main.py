def smallest_divisor_number(number):
    smallest_divisor = 2
    while (number / smallest_divisor) % 1 != 0:
        smallest_divisor += 1
    print('Наименьший делитель, отличный от единицы: ', smallest_divisor)


number_N = int(input('Введите натуральное число N, больше единицы: '))
while number_N <= 1:
    print('Вы ввели неправильное число, попробуйте еще раз!')
    number_N = int(input('Введите натуральное число N, больше единицы: '))

smallest_divisor_number(number_N)


# зачет!
