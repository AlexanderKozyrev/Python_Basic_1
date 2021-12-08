numbers_one = []
numbers_two = []

for _ in range(3):
    number_one = int(input('Введите число в первый список: '))
    numbers_one.append(number_one)

for _ in range(7):
    number_two = int(input('Введите число во второй список: '))
    numbers_two.append(number_two)

numbers_one.extend(numbers_two)

numbers_one = list(set(numbers_one))

print(numbers_one)

