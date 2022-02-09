def flatten(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, int):
            result += number
        elif isinstance(number, (list, tuple)):
            for num in number:
                result += num
        else:
            flatten(number)
    return result
#TODO исправил, но все равно не получается

amount = flatten([[1, 2, [3]], [1], 3])
print(amount)

amount = flatten((1, 2, 3, 4, 5))
print(amount)
