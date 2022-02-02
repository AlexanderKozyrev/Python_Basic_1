def tpl_sort(numbers):
    for number in numbers:
        if int(number) != float(number):
            return numbers
    new_sort = sorted(numbers)
    return new_sort


# TODO функции не вызываем в принте
print(tpl_sort((6, 3, -1, 8, 4, 10, -5)))