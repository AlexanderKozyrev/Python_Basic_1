number_cards = int(input('Введите количество видеокарт: '))
old_list_cards = []
new_list_cards = []
max_card = 0

for number in range(number_cards):
    print(number + 1, 'Видеокарта: ', end='')
    card = int(input())
    old_list_cards.append(card)
    if card > max_card:
        max_card = card

print('Старый список видеокарт: ', old_list_cards)

for card in old_list_cards:
    if card != max_card:
        new_list_cards.append(card)

print('Новый список видеокарт: ', new_list_cards)

# TODO инпут не должен быть пустым
# TODO сообщение что в принте переносим полностью в инпут

# TODO нейминг переменной с list, оно зарезервированное системой, использовать в имени переменной не рекомендуется
# TODO так же как set, dict, tuple в следующих модулях
