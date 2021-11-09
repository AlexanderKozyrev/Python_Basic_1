
print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
if x2 == x1:
    print('Координаты Х первой точки не должны равняться координатам Х второй точки. ')
    x2 = float(input('Введите координаты X еще раз: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
k = y_diff / x_diff
b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)