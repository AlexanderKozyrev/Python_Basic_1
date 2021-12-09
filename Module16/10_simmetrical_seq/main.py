numbers = int(input('Введите количество чисел: '))
num = []

for index in range(numbers):
    number = int(input('Число: '))
    num.append(number)
print('Последовательность: ', end=' ')
for index in range(numbers):
    print(num[index], end=' ')
