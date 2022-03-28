def exceptions(text):
    try:
        text = text.split()
        if len(text) != 3:
            raise IndexError
        if not text[0].isalpha():
            raise NameError
        if '@' and '.' not in text[1]:
            raise SyntaxError
        if not 0 < int(text[2]) < 99:
            raise ValueError
        else:
            with open('registraton_good.log', mode='a', encoding='utf-8') as good:
                good.write(line + '\n')

    except IndexError:
        with open ('registration_bad.log', mode='a', encoding='utf-8') as bad:
            bad.write(line + '     НЕ присутствуют все три поля' + '\n')

    except NameError:
        with open ('registration_bad.log', mode='a', encoding='utf-8') as bad:
            bad.write(line + '     поле имени содержит НЕ только буквы:' + '\n')

    except SyntaxError:
        with open ('registration_bad.log', mode='a', encoding='utf-8') as bad:
            bad.write(line + '     поле емейл НЕ содержит @ и .(точку):' + '\n')

    except ValueError:
        with open ('registration_bad.log', mode='a', encoding='utf-8') as bad:
            bad.write(line + '     поле возраст НЕ является числом от 10 до 99:' + '\n')


with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        exceptions(line)

