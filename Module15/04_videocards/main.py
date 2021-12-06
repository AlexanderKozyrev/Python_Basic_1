number_cards = int(input('Введите количество видеокарт: '))
old_registry_cards = []
new_registry_cards = []
max_card = 0

for number in range(number_cards):
    card = int(input(f'{number + 1} Видеокарта: '))
    old_registry_cards.append(card)
    if card > max_card:
        max_card = card

print('Старый список видеокарт: ', old_registry_cards)

for card in old_registry_cards:
    if card != max_card:
        new_registry_cards.append(card)

print('Новый список видеокарт: ', new_registry_cards)




