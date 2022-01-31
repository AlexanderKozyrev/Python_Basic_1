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

for good, code in goods.items():
    total_price = 0
    total_number = 0
    product_parameters = {}

    for stores in store[code]:
        total_number += stores['quantity']
        total_price += stores['price'] * stores['quantity']

    print(good, '-', total_number, 'шт, стоимость ', total_price, 'руб')



