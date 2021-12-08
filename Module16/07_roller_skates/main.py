number_skates = int(input('Введите количество коньков: '))
sizes_skates = []
sizes_foot = []
people = 0

for skate in range(number_skates):
    size_skate = int(input(f'Размер {skate + 1} пары: '))
    sizes_skates.append(size_skate)

print()
number_foot = int(input('Введите количество людей: '))

for foot in range(number_foot):
    size_foot = int(input(f'Размер ноги {foot + 1} человека: '))
    sizes_foot.append(size_foot)

for size in sizes_foot:
    for skate in sizes_skates:
        if size <= skate:
            people += 1
            sizes_skates.remove(skate)

print()
print('Наибольшее кол-во людей, которые могут взять ролики: ', people)
