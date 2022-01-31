def is_poly(string):
    char = {}
    for letter in string:
        char[letter] = char.get(letter, 0) + 1

    odd_count = 0
    for value in char.values():
        if value % 2 != 0:
            odd_count += 1

    return odd_count <= 1


text = input('Введите строку: ')
if is_poly(text):
    print('Можно сделать палиндром')
else:
    print('Нельзя сделать палиндром')
