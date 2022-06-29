import time


def waiting(fnc):
    time.sleep(4)
    fnc()


@waiting
def get_data():
    print('Идет анализ данных')
