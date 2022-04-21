def square(number):
    for num in range(1, number + 1):
        yield num ** 2


number_n = int(input('Введите число N: '))

gen = square(number_n)
for i_elem in gen:
    print(i_elem, end=' ')
print()

gen = (i_elem ** 2 for i_elem in range(1, number_n + 1))
for i in gen:
    print(i, end=" ")
print()


class MyIter:

    def __init__(self, number):
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        else:
            return self.count ** 2


ny_iter = MyIter(number_n)
for i_elem in ny_iter:
    print(i_elem)
