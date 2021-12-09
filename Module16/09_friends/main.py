friends = int(input('Введите количество друзей: '))
receipts = int(input('Введите количество олговых расписок: '))
registry_friends = []

for i in range(friends):
    registry_friends.append(0)

for receipt in range(receipts):
    print(receipt + 1, 'расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    how_many = int(input('Сколько: '))
    registry_friends[to_whom - 1] += how_many
    registry_friends[from_whom - 1] -= how_many

print('Балнс друзей: ')
for index in range(friends):
    print(index + 1, ':', registry_friends[index])
