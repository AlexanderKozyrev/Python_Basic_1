numbers = int(input('Введите количество заказов: '))
name_dict = {}
for number in range(1, numbers + 1):
    order = input(f'{number} заказ: ').split()
    name_dict[number] = order

print(name_dict)