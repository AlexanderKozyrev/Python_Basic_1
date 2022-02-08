def flatten(a_list):
    result = 0
    for number in a_list:
        if isinstance(number, int):
            result += number
        else:
            flatten(number)
    return result


amount = flatten([[1, 2, [3]], [1], 3])
print(amount)

amount = flatten((1, 2, 3, 4, 5))
print(amount)
