from typing import List


floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

floats_new = list(map(lambda x: round(x**3, 3), floats))
names_new = list(filter(lambda x: len(x) > 4, names))
numbers_new =
print(names_new)