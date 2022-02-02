from random import randint

original_numbers = [randint(0, 10) for _ in range(10)]

print('Оригинальный список: ', original_numbers)

new_numbers = []
for number in range(0, 10, 2):
    new_numbers += [(original_numbers[number], original_numbers[number + 1])]

print('Новый список:', new_numbers)


