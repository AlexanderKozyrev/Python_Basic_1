number_N = int(input("Кол-во элементов: "))
start_list = []

for _ in range(number_N):
    element = input("Введите элемент списка:")
    start_list.append(element)

shift = int(input("Сдвиг: "))
index = 0
while index < number_N - 1:
    empty_place = start_list[index]
    start_list[index] = start_list[index + shift]
    start_list[index + shift] = empty_place
    index += 1

print('Сдвинутый список: ', start_list)

# TODO применить рекомендации данные ранее

