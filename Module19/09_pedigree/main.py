numbers = int(input('Введите количество человек:'))
name_dict = {}
height_dict = {}

for number in range(numbers - 1):
    name_descendant, name_parent = input(f'{number + 1} пара: ').split()
    name_dict[name_descendant] = name_parent
    height_dict[name_descendant] = 0
    height_dict[name_parent] = 0

for i_name in name_dict:
    s_name = i_name
    while s_name in name_dict:
        s_name = name_dict[s_name]
        height_dict[i_name] += 1

for i_dict in sorted(height_dict):
    print(i_dict, height_dict[i_dict])


# TODO применить рекомендации данные ранее

