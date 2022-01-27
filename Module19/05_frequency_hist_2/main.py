text = input('Введите текст: ')
original_dict = {}
inverter_dict = {}

for symbol in text:
    if symbol in original_dict:
        original_dict[symbol] += 1
    else:
        original_dict[symbol] = 1

print('Оригинальный словарь частот:')
for letter in sorted(original_dict):
    print(letter, ':', original_dict[letter])

for number in original_dict.keys():
    if not original_dict[number] in inverter_dict:
        inverter_dict[original_dict[number]] = []
    inverter_dict[original_dict[number]].append(number)

print('Инвертированный словарь частот: ')
for letter in inverter_dict:
    print(letter, ':', inverter_dict[letter])

# TODO применить рекомендации данные ранее
