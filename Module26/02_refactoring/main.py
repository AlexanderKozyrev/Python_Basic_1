list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

for x in list_1:
    for y in list_2:
        result = x * y
        if result == to_find:
            print(f'{x}, {y}, {result}')



