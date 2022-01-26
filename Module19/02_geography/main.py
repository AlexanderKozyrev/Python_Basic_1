numbers_countries = int(input('Количество стран: '))
countries_dict = {}

for i_number in range(0, numbers_countries):
    country = input(f'{i_number + 1} страна: ').split()
    countries_dict[country[0]] = country[1:]

for number in range(1, 4):
    town = input(f'{number} город: ')
    for country in countries_dict:
        if town in countries_dict[country]:
            print(f'Город {town} расположен в стране {country}')
        else:
            print(f'По городу {town} данных нет')
