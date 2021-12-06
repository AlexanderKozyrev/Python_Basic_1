number_containers = int(input('Введите количество контейнеров: '))
weight_containers = []

for number in range(number_containers):
    weight_container = int(input('Введите вес контейнера: '))
    while weight_container > 200:
        weight_container = int(input(' Вес контейнера не должен превышать 200кг, введите вес еще раз '))
    weight_containers.append(weight_container)

new_weight_container = int(input('Введите вес нового контейнера: '))
while new_weight_container > 200:
    new_weight_container = int(input('Вес контейнера не должен превышать 200кг, введите вес еще раз '))

for new_number in range(number_containers):
    if weight_containers[new_number] < new_weight_container:
        print('Номер, куда встанет новый контейнер: ', new_number + 1)
        break

