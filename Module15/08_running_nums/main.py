number_N = int(input('Кол-во элементов: '))
start_registry = []

for _ in range(number_N):
    element = input('Введите элемент списка:')
    start_registry.append(element)

shift = int(input('Сдвиг: '))
index = 0
while index < number_N - 1:
    empty_place = start_registry[index]
    start_registry[index] = start_registry[index + shift]
    start_registry[index + shift] = empty_place
    index += 1

print('Сдвинутый список: ', start_registry)



