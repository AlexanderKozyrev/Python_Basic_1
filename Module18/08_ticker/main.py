line_1 = input('Первая строка: ')
line_2 = input('Вторая строка: ')

if line_1 == line_2:
    print('Строки идентичны.')
elif len(line_1) != len(line_2):
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
else:
    shift = 1
    may_shift = False
    for _ in range(len(line_2) - 1):
        line_2 = line_2[-1] + line_2[:-1]
        if line_2 == line_1:
            may_shift = True
            print('Первая строка получается из второй со сдвигом ', shift)
            break
        else:
            shift += 1
    if not may_shift:
        print('Первую строку нельзя получить из второй с помощью циклического сдвига.')


