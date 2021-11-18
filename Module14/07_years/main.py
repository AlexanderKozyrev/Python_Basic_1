def three_identical_numbers(number):
    number_4 = number % 10
    number_3 = (number % 100) // 10
    number_2 = (number // 100) % 10
    number_1 = number // 1000

    if (number_1 == number_2 == number_3 or number_1 == number_2 == number_4 or number_1 == number_3 == number_4
        or number_2 == number_3 == number_4):
        print(number)


years_one = int(input('Введите первый год: '))
years_two = int(input('Введите второй год: '))
print('Года от ', years_one, 'до ', years_two, 'с тремя одинаковыми цифрами: ')
while years_one != years_two:
    three_identical_numbers(years_one)
    years_one += 1

