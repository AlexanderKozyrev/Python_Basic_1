numbers_file = open('numbers.txt', 'r')
answer = 0

for number in numbers_file:
    for num in number.split():
        answer += int(num)


answer_file = open('answer.txt', 'w')
answer_file.write(str(answer))
numbers_file.close()
answer_file.close()
