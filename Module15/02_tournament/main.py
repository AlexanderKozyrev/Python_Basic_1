
number_names = ['Артемий', 'Борис', 'Влад',
                'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
new_number_names = []

for number in range(8):
    if (number + 1) % 2 == 0:
        new_number_names.append(number_names[number])

print(new_number_names)