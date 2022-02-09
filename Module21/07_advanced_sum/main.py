def flatten(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, int):
            result += number
        elif isinstance(number, (list, tuple)):
            for x in number:
                result += x
        else:
            flatten(number)
    return result


amount = flatten([[1, 2, [3]], [1], 3])
print(amount)

amount = flatten((1, 2, 3, 4, 5))
print(amount)
