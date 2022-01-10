import random

first_team = [round((random.uniform(5, 10)), 2) for _ in range(20)]
second_team = [round((random.uniform(5, 10)), 2) for _ in range(20)]
winners = []

for number in range(20):
    if first_team[number] > second_team[number]:
        winners.append(first_team[number])
    else:
        winners.append(second_team[number])

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победителя тура: ', winners)

