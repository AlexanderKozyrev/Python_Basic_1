import os

count_str = 0

files = os.listdir()

for file in files:
    if os.path.isfile(file):
        if file.endswith('.py'):
            with open(file) as fale:
                strings = fale.read().split('\n')
                for string in strings:
                    if string.strip() and not string.startswith('#'):
                        count_str += 1

print('Всего строк:', count_str)
