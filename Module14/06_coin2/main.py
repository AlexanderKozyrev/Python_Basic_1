print('Введите координаты монетки:')
number_X = float(input('X: '))
number_Y = float(input('Y: '))
radius = float(input('Введите радиус: '))

if (number_X ** 2 + number_Y ** 2) ** 0.5 <= radius:
    print("Монетка где-то рядом")
else:
    print('Монетки в области нет')

# зачет!
