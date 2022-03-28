import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except Exception:
            print("Что-то пошло не так с функциями")
        number = random.randint(0, 100)
        my_list = sorted([res1, res2, number])
        with open('result.txt', 'a', encoding='utf-8') as file_2:
            file_2.write(' '.join(str(my_list)) + '\n')


