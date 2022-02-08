def hanoi_towers(number, start=1, finish=3):
    if number == 1:
        print("Перенести диск 1 со стержня", start, "на стержень", finish)
    else:
        temp = (6 - start) - finish
        hanoi_towers(number - 1, start, temp)
        print("Перенести диск", number, "со стержня", start, "на стержень", finish)
        res = (number - 1, temp, finish)
        print("Перенести диск", number-1, "со стержня", temp, "на стержень", finish)
        return res


numbers = int(input('Введите количество дисков: '))
hanoi_towers(numbers)
