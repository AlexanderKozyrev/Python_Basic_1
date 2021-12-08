rank_one = []
rank_two = []

for height in range(160, 178, 2):
    rank_one.append(height)

for height in range(162, 183, 3):
    rank_two.append(height)

rank_one.extend(rank_two)

for i in range(len(rank_one)):
    for j in range(i + 1, len(rank_one)):
        if rank_one[j] < rank_one[i]:
            rank_one[i], rank_one[j] = rank_one[j], rank_one[i]

print('Отсортированный список: ', rank_one)

