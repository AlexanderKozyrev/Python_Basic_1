import random

number_N = int(input('Кол-во чисел в списке: '))
before_compression = [random.randint(0, 2) for _ in range(number_N)]
after_compression = []

for number in range(number_N):
    if before_compression[number] != 0:
        after_compression.append(before_compression[number])

print('Список до сжатия: ', before_compression)
print('Список после сжатия: ', after_compression)


