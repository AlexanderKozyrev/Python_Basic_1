nice_order = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def expands_order(numbers):
    result = []
    for number in numbers:
        if isinstance(number, int):
            result.append(number)
        else:
            result.extend(expands_order(number))
    return result


new_nice_order = expands_order(nice_order)
print(new_nice_order)
