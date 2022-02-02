recordings = int(input('Сколько записей вносится в протокол? '))
protocol = {}
winners = {}

print('Записи (результат и имя): ')
for record in range(1, recordings + 1):
    result, name = input(f'{record} запись: ').split()
    result = int(result)
    protocol[f'{record} запись:'] = result, name
    if name in winners:
        if result > winners[name][0]:
            winners[name][0] = result
            winners[name][1] = record
    else:
        winners[name] = [result, record]
winner = list(winners.items())

print(winners)
print(winner)


