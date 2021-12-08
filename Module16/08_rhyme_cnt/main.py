number_people = int(input('Количество человек: '))
number = int(input('Какое число в считалке? '))
print('Значит выбывает каждый ', number, 'человек')
retires = 0
numbers_people = list(range(1, number_people + 1))


for _ in range(number_people - 1):
    print('Текущий круг людей: ', numbers_people)
    beginning = retires % len(numbers_people)
    retires = (beginning + number - 1) % len(numbers_people)
    print('Начало отсчета с номера: ', numbers_people[beginning])
    print('Выбывает человек под номером: ', numbers_people[retires])
    numbers_people.remove(numbers_people[retires])
    print()

print('Остался человек под номером', numbers_people[0])


