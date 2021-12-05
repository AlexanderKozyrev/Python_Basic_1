number_cells = int(input('Введите количество клеток: '))
unsuitable_values = []

for number in range(number_cells):
    print('Эффективность', number + 1, 'клетки: ')
    effectiveness = int(input(''))
    if effectiveness < number:
        unsuitable_values.append(effectiveness)

print('Неподходящие значения', unsuitable_values)

# TODO инпут не должен быть пустым
# TODO сообщение что в принте переносим полностью в инпут

