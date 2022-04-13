import random


def one_day():

    if random.randint(1, 10) != 1:
        return random.randint(1, 7)
    else:
        with open('karma.log', 'a', encoding='utf-8') as karma_log:
            name_er = random.choice(['KillError', 'DrunkError', 'CarCrashError', 'GluttonyError', 'DepressionError'])
            karma_log.write(f'\n{name_er}')
            return False


karma = 0

while karma < 500:
    if one_day():
        karma += one_day()
        print(karma)

print('Просветление достигнуто')