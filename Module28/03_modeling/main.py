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
        return self.a + self.b + self.c


class Cube(Figure):
    def __init__(self, r):
        super().__init__('Куб')
        self.sq = (r ** 2) * 6
        self.pr = r * 12


class Pyramid(Figure):
    def __init__(self, r, a, b, c):
        self.f_name = 'pyramid'
        self.sq =
        self.pr =


p = Pyramid(2, 4, 6, 8)
print(p.pr)

p = Cube(5)
print(p.pr)