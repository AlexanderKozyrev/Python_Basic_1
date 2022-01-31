students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def interests(dictionary):
    lst = []
    string = 0
    couples = []
    for number, info in dictionary.items():
        couples += (number, info['age'])
        lst += (info['interests'])
        string += len(info['surname'])
    return lst, string, couples


my_lst, length, pairs = interests(students)

print('Список пар ID студента - Возраст:', pairs)
print('Полный список интересов всех студентов: ', my_lst)
print('Общая длина всех фамилий студентов: ', length)


