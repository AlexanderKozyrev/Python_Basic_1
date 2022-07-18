import re


car_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
private_cars = re.findall(r'\D\d{3}\D{2}\d{2,3}', car_numbers)
taxi_cars = re.findall(r'\w{2}\d{3}\d{2,3}', car_numbers)

print('Список номеров частных автомобилей: ', private_cars)
print('Список номеров такси: ', taxi_cars)
