class Cars:

    def __init__(self, x_coord, y_coord, corner):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.corner = corner

    def move(self, dist):
        self.x_coord = self.x_coord + dist * cos(self.corner)
        self.y_coord = self.y_coord + dist * sin(self.corner)


class Bus(Cars):
    money = 0
    passengers = 0

    def enter(self, number):
        self.passengers += number
        print(f'В автобус вошло {number} пассажиров, всего в автобусе {self.passengers} пассажиров')

    def exited(self, number):
        self.passengers -= number
        print(f'Из автобуса вышло {number} пассажиров, всего в автобусе {self.passengers} пассажиров')

    def move(self, dist):



