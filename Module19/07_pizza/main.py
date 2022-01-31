numbers = int(input('Введите количество заказов: '))
name_dictionary = {}
for number in range(1, numbers + 1):
    order = input(f'{number} заказ: ').split()
    name_dictionary[number] = order

print(name_dictionary)


