import itertools


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in itertools.combinations_with_replacement(numbers, 4):
    print(number)