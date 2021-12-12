def is_palindrom(num_list):
    revers_list = []
    for i_num in range(len(num_list) - 1, -1, -1):
        revers_list.append(num_list[i_num])
    if num_list == revers_list:
        return True
    else:
        return False

numbers = int(input('Введите количество чисел: '))
num = []
new_num = []
answer = []

for index in range(numbers):
    number = int(input('Число: '))
    num.append(number)
print('Последовательность: ', end=' ')
for index in range(numbers):
    print(num[index], end=' ')

for number in range(numbers):
    for i in range(number, numbers):
        new_num.append(num[i])
    if is_palindrom(new_num):
        for i_answer in range(0, number):
            answer.append(num[i_answer])
        answer.reverse()
        break
    new_num = []

print('Нужно чисел для палиндрома: ', len(answer))
print('Список этих чисел: ', answer)

