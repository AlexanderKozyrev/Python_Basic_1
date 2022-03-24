file = open('first_tour.txt', 'r', encoding='utf=8')
scores = file.readline()
new_list = []

for line in file:
    new_line = line.split()

    if new_line != [] and new_line[-1] > scores:
        new_list.append(new_line)
file.close()

count = str(len(new_list))

new_list.sort(key=lambda a: int(a[-1]), reverse=True)

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    for i in new_list:
        name_sim = str(i[1][0]) + '. ' + str(i[0]) + ' ' + str(i[-1])
        f_out.write(name_sim + '\n')



