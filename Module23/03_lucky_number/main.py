import random


class MyFirstException(Exception):
    pass


numbers_sum = 0
try:
    while numbers_sum < 777:
        number = int(input('Введите число:'))
        numbers_sum += number
        probability = random.randint(1, 13)
        if probability == 1:
            raise MyFirstException

        with open('out_file.txt', 'a') as file:
            file.write(str(number) + '\n')

    print("Вы успешно выполнили условие для выхода из порочного цикла!")

except MyFirstException:
    print('Вас постигла неудача!')
