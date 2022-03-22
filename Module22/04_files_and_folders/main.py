import os

path = input('Пожалуйста, введите путь до директории:')
total_size = 0
path, dirs, files = next(os.walk(path))
for name in files:
    fp = os.path.join(path, name)
    total_size += os.path.getsize(fp)

print('Размер каталога (в Кб): ', total_size / 1024)
print('Количество подкаталогов: ', len(dirs))
print('Количество файлов: ', len(files))
