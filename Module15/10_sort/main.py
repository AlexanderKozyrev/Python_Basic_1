number_N = int(input("Кол-во элементов: "))
start_list = []

for _ in range(number_N):
    element = input("Введите элемент списка:")
    start_list.append(element)

for i in range(number_N - 1):
    minimum = i

    for j in range(i + 1, number_N):
        if start_list[j] < start_list[minimum]:
            minimum = j
    start_list[minimum], start_list[i] = start_list[i], start_list[minimum]

print('Отсортированный список: ', start_list)


# TODO применить рекомендации данные ранее по неймингу
