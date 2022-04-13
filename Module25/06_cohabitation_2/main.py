from random import randint, choices


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
    food_eaten = 0

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
        self.food_eaten += meal


    def day(self):
        if self.satiety <= 0:
            print(f'{self.name} умер')
            raise SystemExit
        if Home.dirt > 90:
            self.happiness -= 10
        if self.happiness < 10:
            print(f'{self.name} умер')
            raise SystemExit


class Husband(People):
    money_work = 0

    def play(self):
        print(f'{self.name} играет')
        self.satiety -= 10
        self.happiness += 20

    def work(self):
        print(f'{self.name} работает')
        self.satiety -= 10
        Home.money += 150
        self.money_work += 150

    def day(self):
        number = randint(1, 4)
        if number == 1:
            self.eat()
        elif number == 2:
            self.petting_cat()
        elif number == 3:
            self.play()
        else:
            self.work()


class Wife(People):
    fur_coat = 0

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
        self.fur_coat += 1

    def clean_house(self):
        print(f'{self.name} убралась в доме')
        self.satiety -= 10
        Home.dirt -= randint(1, 100)

    def day(self):
        number = randint(1, 5)
        if number == 1:
            self.eat()
        elif number == 2:
            self.petting_cat()
        elif number == 3:
            self.buy_groceries()
        elif number == 4:
            self.buy_fur_coat()
        else:
            self.clean_house()


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

    def cat_day(self):
        if self.satiety <= 0:
            print(f'Кот {self.name} умер')
            raise SystemExit
        number = randint(1, 3)
        if number == 1:
            self.eat()
        elif number == 2:
            self.sleep()
        else:
            self.tear_wallpaper()

home = Home()
man = Husband('Саша')
woman = Wife('Марина')
cat = Cat('Барсик')

for _ in range(365):
    home.dirt += 5
    man.day()
    woman.day()
    cat.cat_day()
    print()

print(f'За год было заработано {man.money_work} денег, {man.food_eaten + woman.food_eaten} сьедено еды, {woman.fur_coat} куплено шуб')