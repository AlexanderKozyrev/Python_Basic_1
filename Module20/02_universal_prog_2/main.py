def is_prime(sumbol):
    divisors = 0
    for number in range(1, sumbol + 1):
        if sumbol % number == 0:
            divisors += 1
    if divisors == 2:
        return sumbol


def crypto(text):
    new_text = []
    for number, meaning in enumerate(text):
        if is_prime(number):
            new_text += meaning
    return new_text

# TODO функции не вызываем в принте
print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(crypto('О Дивный Новый мир!'))