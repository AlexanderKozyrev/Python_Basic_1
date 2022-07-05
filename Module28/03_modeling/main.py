import math


class Figure:
    figure_name = 'Фигура'

    def __init__(self, figure_name: str) -> None:
        self.figure_name = figure_name

    def show_name(self) -> str:
        print(self.figure_name)


class Square(Figure):
    def __init__(self, side: float) -> None:
        super().__init__('Квадрат')
        self.side = side

    def get_square(self) -> float:
        return self.side ** 2

    def get_perimeter(self) -> float:
        return 4 * self.side


class Triangle(Figure):
    def __init__(self, footing: float, height: float) -> None:
        super().__init__('Треугольник')
        self.footing = footing
        self.height = height

    def get_square(self) -> float:
        return self.footing * self.height / 2

    def get_perimeter(self) -> float:
        return self.footing + 2 * math.sqrt((self.footing / 2) ** 2 + self.height ** 2)


class Cube(Square):
    def __init__(self, side: float) -> None:
        super().__init__('Квадрат')
        self.side = side

    def get_square(self) -> float:
        return self.side ** 2 * 6


class Pyramid(Triangle):
    def __init__(self, footing: float, height: float) -> None:
        super().__init__('Треугольник')
        self.footing = footing
        self.height = height

    def get_square(self) -> float:
        return (self.footing * self.height / 2) * 4 + self.height ** 2


