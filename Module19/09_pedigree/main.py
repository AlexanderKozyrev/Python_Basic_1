numbers = int(input('Введите количество человек:'))
name_dictionary = {}
height_dictionary = {}

for number in range(numbers - 1):
    name_descendant, name_parent = input(f'{number + 1} пара: ').split()
    name_dictionary[name_descendant] = name_parent
    height_dictionary[name_descendant] = 0
    height_dictionary[name_parent] = 0

for name in name_dictionary:
    s_name = name
    while s_name in name_dictionary:
        s_name = name_dictionary[s_name]
        height_dictionary[name] += 1

# TODO код падает
for dictionary in sorted(height_dictionary):
    print(dictionaryt, height_dictionary[dictionary])


