text = 'abdd'
numbers = (10, 20, 30, 40)
text_numbers = zip(text, numbers)
print(text_numbers)
for couples in text_numbers:
    print(couples)

pairs = ((text[elem], numbers[elem]) for elem in range(min(len(text), len(numbers))))
print(pairs)

for elem in pairs:
    print(elem)
