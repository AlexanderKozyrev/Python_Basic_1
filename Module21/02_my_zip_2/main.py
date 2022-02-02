def pairs(text, numbers):
    my_pairs = ((text[elem], numbers[elem]) for elem in range(min(len(text), len(numbers))))
    return my_pairs


my_text = 'abdd'
my_numbers = (10, 20, 30, 40)

for element in pairs(my_text, my_numbers):
    print(element)
