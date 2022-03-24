zen_file = open('zen.txt', 'r')
zen_list = []

for line in zen_file:
    zen_list.append(line)

for line in zen_list[::-1]:
    print(line)
