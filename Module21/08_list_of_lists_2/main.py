nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def expands_lists(a_list):
    result = []
    for number in a_list:
        if isinstance(number, int):
            result.append(number)
        else:
            result.extend(expands_lists(number))
    return result


new_nice_list = expands_lists(nice_list)
print(new_nice_list)