from random import randint, choice

NAMES = ['Алексей', 'Женя', 'Иван', 'Петр', 'Семен', 'Антон', 'Максим']
SURNAMES = ['Первый', 'Второй', 'Иванов', 'Четвертый', 'Петров']


def generate_person():
    name = choice(NAMES)
    surname = choice(SURNAMES)
    age = randint(20, 50)
    return name, surname, age


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Меня зовут {self.__name} {self.__surname}. Мой возраст - {self.__age}'


class Employee(Person):

    def payment_calculation(self):
        print('Метод расчета з/п:')

    def __str__(self):
        return super().__str__() + f'\nМоя зарплата {self.payment_calculation()}'


class Manager(Employee):

    def payment_calculation(self):
        payment = 13000
        return payment


class Agent(Employee):
    sales: int

    def payment_calculation(self):
        payment = 5000 + self.sales * 0.05
        return payment


class Worker(Employee):
    days: int

    def payment_calculation(self):
        payment = 100 * self.days
        return payment


employees = list()

for _ in range(3):
    employees.append(Manager(*generate_person()))

for _ in range(3):
    agent = Agent(*generate_person())
    agent.sales = randint(2000, 10000)
    employees.append(agent)

for _ in range(3):
    worker = Worker(*generate_person())
    worker.days = randint(20, 50)
    employees.append(worker)

for emp in employees:
    print(emp)
