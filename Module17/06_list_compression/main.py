import random

number_N = int(input('Кол-во чисел в списке: '))
before_compression = [random.randint(0, 2) for _ in range(number_N)]
after_compression = []

for i in range(number_N):
    if before_compression[i] != 0:
        after_compression.append(before_compression[i])

print('Список до сжатия: ', before_compression)
print('Список после сжатия: ', after_compression)