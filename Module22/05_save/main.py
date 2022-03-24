import os

text = str(input(f'Введите строку: \n'))
way = str(input(
    f'Куда хотите сохранить документ? Введите последовательность папок (через пробел): \n'))
filename = str(input(f'Введите имя файла: \n'))

abs_path = os.path.abspath(filename)
check_file = os.path.exists(abs_path)

if check_file:
    ans_q = input(f'Вы действительно хотите перезаписать файл? \n')
    if ans_q == 'да':
        with open(filename, 'w') as file_object:
            file_object.write(text)
            print(f'Файл успешно перезаписан!')
    else:
        print(f'Файл не перезаписан!')
else:
    with open(filename, 'w') as file_object:
        file_object.write(text)
        print(f'Файл успешно сохранён!')