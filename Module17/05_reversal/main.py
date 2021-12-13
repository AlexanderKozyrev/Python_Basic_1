line = input('Введите строку: ')

line = line[line.find('h') + 1:]
line = line[:line.rfind('h')]

print('Развернутая последовательность между первым и последним h: ', line[::-1])