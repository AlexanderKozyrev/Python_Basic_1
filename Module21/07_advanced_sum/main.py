def flatten(numbers):
    result = 0
    for number in numbers:
        if isinstance(number, int):
            result += number
        # тут делаем elif и вставляем
        #         elif isinstance(i_elem, (list, tuple)):
        #             for x in i_elem:
        #                 total_sum += my_sum(x)
        else:
            flatten(number)
    return result


amount = flatten([[1, 2, [3]], [1], 3])
print(amount)

amount = flatten((1, 2, 3, 4, 5))
print(amount)
