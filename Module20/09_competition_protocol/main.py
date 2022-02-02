recordings = int(input('Сколько записей вносится в протокол? '))
protocol = {}
winners = {}

print('Записи (результат и имя): ')
for record in range(1, recordings + 1):
    result, name = input(f'{record} запись: ').split()
    result = int(result)
    protocol[f'{record} запись:'] = result, name
    # TODO вот так должно работать
    if name in winners:
        if result > winners[name]:
            winners[name] = result
    else:
        winners[name] = result
winner = list(winners.items())

print(winners)
print(winner)


