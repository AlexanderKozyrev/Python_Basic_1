# TODO здесь писать код
number_N = int(input('Введите целое число: '))
score_odd = []

for number in range(number_N + 1):
    if number // 2 == 0:
        score_odd.append(number)

print(score_odd)
