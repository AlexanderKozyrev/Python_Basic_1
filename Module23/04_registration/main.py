def exceptions(text):
    try:
        text = text.split()
        if len(text) != 3:
            raise IndexError
        if text[0].isalpha() = False:
            raise NameError



    except IndexError:
        print('НЕ присутствуют все три поля')
    except NameError:


with open('registrations.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(len(line))

