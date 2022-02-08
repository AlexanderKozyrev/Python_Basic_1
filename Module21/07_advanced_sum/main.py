def flatten(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, int):
            result += number
        else:
            flatten(number)
    return result
#TODO как сделать чтобы функция складывала весь результат


amount = flatten([[1, 2, [3]], [1], 3])
print(amount)

amount = flatten((1, 2, 3, 4, 5))
print(amount)
