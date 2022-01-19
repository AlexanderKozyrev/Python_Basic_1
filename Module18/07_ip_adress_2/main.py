ip_address = input('Введите IP: ').split('.')

if not len(ip_address) == 4:
    print('Адрес - это четыре числа, разделенные точками')
for number in ip_address:
    if not number.isdigit():
        print(number, 'не целое число')
        break
    if not int(number) <= 255:
        print(number, 'превышает 255')
        break
    if not int(number) >= 0:
        print(number, 'число не должно быть меньше 0')
        break
else:
    print('IP-адрес корректен')
