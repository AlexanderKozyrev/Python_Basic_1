from random import randint, choice


class Home:

    money = 100
    meal = 50
    meal_cat = 30
    dirt = 0

    def __str__(self):
        return f'Денег - {self.money}\nЕда - {self.meal}\nЕда Кота - {self.meal_cat}\nГрязь - {self.dirt}\n'


class People:
    satiety = 30
    happiness = 100

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Имя - {self.name}\nСытость - {self.satiety}\nСчастье - {self.happiness}\n'

    def petting_cat(self):
        print(f'{self.name} погладил кота')
        self.happiness += 5
        self.satiety -= 10

    def eat(self):
        meal = randint(1, 30)
        print(f'{self.name} покушал {meal} еды')
        self.satiety += meal
        Home.meal -= meal


class Husband(People):

    def play(self):
        print(f'{self.name} играет')
        self.satiety -= 10
        self.happiness += 20

    def work(self):
        print(f'{self.name} работает')
        self.satiety -= 10
        Home.money += 150


class Wife(People):

    def buy_groceries(self):
        print(f'{self.name} купила продукты')
        self.satiety -= 10
        Home.meal += 10
        Home.meal_cat += 10
        Home.money -= 20

    def buy_fur_coat(self):
        print(f'{self.name} купила шубу')
        self.satiety -= 10
        Home.money -= 350
        self.happiness += 60

    def clean_house(self):
        print(f'{self.name} убралась в доме')
        self.satiety -= 10
        Home.dirt -= randint(1, 100)


class Cat:
    satiety = 30

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Кот - {self.name}\nСытость - {self.satiety}\n'

    def eat(self):
        meal = randint(1, 10)
        print(f'Кот {self.name} покушал {meal} еды')
        self.satiety += meal * 2
        Home.meal_cat -= meal

    def sleep(self):
        print(f'Кот {self.name} поспал')
        self.satiety -= 10

    def tear_wallpaper(self):
        print(f'Кот {self.name} дерет обои')
        self.satiety -= 10
        Home.dirt += 5

home = Home()
man = Husband('Том')
woman = Wife('Марина')
print(woman)
cat = Cat('Барсик')
print(cat)
print(home)
man.eat()
print(man)
print(home)
for _ in range(365):
    choice[man.eat(), man.petting_cat()]
    print(man)
