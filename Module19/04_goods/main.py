goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# TODO используем .items() у словаря и получаем сразу в заголовке цикла имя и код товара
for good in goods:
    total_price = 0
    total_number = 0

    # TODO тут мы получаем словарь параметры_продукта из store[code] одним циклом без дополнительных условий

    for i_store in store[goods[good]]:
        total_price += j_store['quantity'] * j_store['price']
        total_number += j_store['quantity']

    print(good, '-', total_number, 'шт, стоимость ', total_price, 'руб')


# TODO применить рекомендации данные ранее, + код падает

