
def function_number(number):
    if number == 0:
        return number
    new_number = number - function_number(number - 1)
    print(number)
    return new_number


my_number = int(input('Введите число: '))
function_number(my_number)

