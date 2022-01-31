numbers_countries = int(input('Количество стран: '))
countries = {}

for number in range(0, numbers_countries):
    country = input(f'{number + 1} страна: ').split()
    countries[country[0]] = country[1:]

# TODO сокращений быть недолжно
for num in range(1, 4):
    town = input(f'{num} город: ')
    for country in countries:
        if town in countries[country]:
            print(f'Город {town} расположен в стране {country}')
        else:
            print(f'По городу {town} данных нет')
