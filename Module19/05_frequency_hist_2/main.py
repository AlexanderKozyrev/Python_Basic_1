text = input('Введите текст: ')
original_dictionary = {}
inverter_dictionary = {}

for symbol in text:
    if symbol in original_dictionary:
        original_dictionary[symbol] += 1
    else:
        original_dictionary[symbol] = 1

print('Оригинальный словарь частот:')
for letter in sorted(original_dictionary):
    print(letter, ':', original_dictionary[letter])

for number in original_dictionary.keys():
    if not original_dictionary[number] in inverter_dictionary:
        inverter_dictionary[original_dictionary[number]] = []
    inverter_dictionary[original_dictionary[number]].append(number)

print('Инвертированный словарь частот: ')
for letter in inverter_dictionary:
    print(letter, ':', inverter_dictionary[letter])

