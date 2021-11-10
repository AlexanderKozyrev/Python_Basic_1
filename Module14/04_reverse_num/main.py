def coup_number(number):
    revers_number = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        revers_number = revers_number * 10
        revers_number = revers_number + digit
    return revers_number

number_N = float(input('Введите первое число: '))
number_K = float(input('Введите второе число: '))

number_N_whole_part = number_N // 1
number_N_fractional_part = number_N % 1
number_N_whole_part_revers = coup_number(number_N_whole_part)
number_N_fractional_part_revers = coup_number(number_N_fractional_part)
while number_N_fractional_part_revers > 1:
    number_N_fractional_part_revers /= 10
revers_number_N = number_N_whole_part_revers + number_N_fractional_part_revers
print('Первое число наоборот: ', revers_number_N)

number_K_whole_part = number_K // 1
number_K_fractional_part = number_K % 1
number_K_whole_part_revers = coup_number(number_K_whole_part)
number_K_fractional_part_revers = coup_number(number_K_fractional_part)
while number_K_fractional_part_revers > 1:
    number_K_fractional_part_revers /= 10
revers_number_K = number_K_whole_part_revers + number_K_fractional_part_revers
print('Второе число наоборот: ', revers_number_K)

summa_revers_numbers = revers_number_N + revers_number_K
print('Сумма: ', summa_revers_numbers)