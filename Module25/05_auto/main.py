import random


class Car:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.distance = 0

    def rotate(self, angle):
        self.direction += angle
        # keep angle in (-360, 360)
        self.direction %= 360

    def move(self, distance):
        direction_rad = math.radians(self.direction)
        self.x += distance * math.cos(direction_rad)
        self.y += distance * math.sin(direction_rad)

    def __str__(self):
        lines = [
            f'Транспортное средство находится в координатах:',
            f'x : {round(self.x, 2)}',
            f'y : {round(self.y, 2)}',
            f'направление : {round(self.direction, 2)}',
            f'пройденное расстояние : {round(self.distance, 2)}'
        ]
        return '\n'.join(lines)


class Bus(Car):
    PAY_COEFF = 0.01
    MAX_PASSENGERS = 60

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def move(self, distance):
        self.money += Bus.PAY_COEFF * self.passengers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.passengers > Bus.MAX_PASSANGERS:
            print('Достигнута максимальная вместимость автобуса')
            print('Уехать смогли только {:d}'.format(Bus.MAX_PASSANGERS - self.passengers))
            print('Остались {:d}'.format(passengers - (Bus.MAX_PASSANGERS - self.passengers)))
            passengers = Bus.MAX_PASSANGERS - self.passengers
        return passengers

    def exit(self, passengers):
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            passengers = self.passengers

        return passengers

    def __str__(self):
        lines = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров',
            f'У водителя {round(self.money, 2)} денег',
        ]
        return '\n'.join(lines)


def get_init_coords():
    x = random.randint(-9, 9)
    y = random.randint(-9, 9)
    direction = random.randint(0, 359)
    return x, y, direction


def main():
    print('Проверим класс Car')
    car_actions = random.randint(3, 5)
    x, y, direction = get_init_coords()
    car = Car(x, y, direction)
    print(str(car))

    for _ in range(car_actions):
        action = random.randint(1, 2)
        if action == 1:
            distance = random.randint(1, 10)
            car.move(distance)
        elif action == 2:
            angle = random.randint(1, 359)
            car.rotate(angle)

        print(str(car))

    print('Проверим класс Bus')
    bus_actions = random.randint(3, 5)
    x, y, direction = get_init_coords()
    bus = Bus(x, y, direction)
    print(str(bus))
    print()
    for _ in range(bus_actions):
        action = random.randint(1, 4)
        if action == 1:
            distance = random.randint(1, 10)
            bus.move(distance)
        elif action == 2:
            angle = random.randint(1, 359)
            bus.rotate(angle)
        elif action == 3:
            passengers = random.randint(1, 50)
            bus.enter(passengers)
        elif action == 4:
            passengers = random.randint(1, 50)
            bus.exit(passengers)

        print(str(bus))
        print()

