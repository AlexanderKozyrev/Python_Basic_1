def summa_numbers(number):
    sum_number = 0
    while number !=0:
        sum_number += number % 10
        number = number // 10
    return sum_number

def counts_number(number):
    counts_num = 0
    while number != 0:
        number = number // 10
        counts_num += 1
    return counts_num

number_N = int(input('Введите целое положительное число: '))
print('Сумма цифр числа равна: ', summa_numbers(number_N))
print('Количество цифр в числе равна: ', counts_number(number_N))
difference_summy_quantity = summa_numbers(number_N) - counts_number(number_N)
print('Разность суммы и количества цифр: ', difference_summy_quantity)
