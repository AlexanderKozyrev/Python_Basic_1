def move(n, start=1, finish=3):
    if n == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = (6 - start) - finish
        move(n - 1, start, temp)
        print("Перенести диск", n, "со стержня", start, "на стержень", finish)
        res = (n - 1, temp, finish)
        print("Перенести диск", n-1, "со стержня", temp, "на стержень", finish)
        return res


numbers = int(input('Введите количество дисков: '))
move(numbers)
