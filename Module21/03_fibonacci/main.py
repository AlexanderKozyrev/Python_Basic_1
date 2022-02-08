def numbers_fibonacci(pos_num):
    num_one = 0
    num_two = 1
    exitus = 0
    for _ in range(pos_num - 1):
        exitus = num_one + num_two
        num_one = num_two
        num_two = exitus
    return exitus


position = int(input('Введите позицию числа в ряде Фибоначчи: '))
num_fibonacci = numbers_fibonacci(position)

print(num_fibonacci)
