families = {
    ('Сидоров', 'Павел'): 35,
    ('Сидорова', 'Алина'): 30,
    ('Петров', 'Павел'): 80,
    ('Петрова', 'Регина'): 14,
    ('Сидоров', 'Никита'): 12,

}

surname = input('Введите фамилию: ').lower()

for name, numbers in families.items():
    if surname in name[0].lower() or name[0].lower() in surname:
        print(name, numbers)






