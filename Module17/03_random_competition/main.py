import random

first_team = [round((random.uniform(5, 10)), 2) for _ in range(20)]
second_team = [round((random.uniform(5, 10)), 2) for _ in range(20)]
winners = []

for i in range(20):
    if first_team[i] > second_team[i]:
        winners.append(first_team[i])
    else:
        winners.append(second_team[i])

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победителя тура: ', winners)