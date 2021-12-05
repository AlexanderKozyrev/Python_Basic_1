
number_names = ['Артемий', 'Борис', 'Влад',
                'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_number_names = []

# TODO используйте функцию enumerate() сразу в заголовке цикла получите index, name - две переменные сразу
# TODO связку range + len по возможности не используем
# TODO когда можно проитерироваться по списку и получить сразу элемент

for number in range(8):
    if (number + 1) % 2 == 0:
        new_number_names.append(number_names[number])

print(new_number_names)


