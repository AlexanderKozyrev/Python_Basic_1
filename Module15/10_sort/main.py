number_N = int(input("Кол-во элементов: "))
start_registry = []

for _ in range(number_N):
    element = input("Введите элемент списка:")
    start_registry.append(element)

for i in range(number_N - 1):
    minimum = i

    for j in range(i + 1, number_N):
        if start_registry[j] < start_registry[minimum]:
            minimum = j
    start_registry[minimum], start_registry[i] = start_registry[i], start_registry[minimum]

print('Отсортированный список: ', start_registry)



