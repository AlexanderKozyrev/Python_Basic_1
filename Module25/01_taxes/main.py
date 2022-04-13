class Property:
    bet_nalog = 0

    def __init__(self, worth):
        self.worth = worth

    def nalog(self):
        return self.worth / self.bet_nalog


class Appartment(Property):

    bet_nalog = 1000


class Car(Property):
    bet_nalog = 200


class CountryHouse(Property):
    bet_nalog = 500


money = int(input('Введите количество денег: '))

money_appartment = int(input('Введите стоимость квартиры '))
appartment = Appartment(money_appartment)

money_car = int(input('Введите стоимость машины '))
car = Car(money_car)

money_countryHouse = int(input('Введите стоимость квартиры '))
countryHouse = CountryHouse(money_countryHouse)

print(f'Налог на квартиру: {appartment.nalog()}\n'
      f'Налог на машину : {car.nalog()}\n'
      f'Налог на дом {countryHouse.nalog()}')

if money < (appartment.nalog() + car.nalog() + countryHouse.nalog()):
    no_money = (appartment.nalog() + car.nalog() + countryHouse.nalog()) - money
    print(f'Для оплаты всех налогов не хватает {no_money} руб.')
else:
    print('Денег хватает на оплату всех налогов')