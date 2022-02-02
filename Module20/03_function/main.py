def slicer(text, number):
    if text.count(number) == 0:
        return ()
    elif text.count(number) == 1:
        new_text = text[text.index(number):]
        return new_text
    else:
        new_text = text[(text.index(number)):(text.index(number, (text.index(number) + 1)) + 1)]
        return new_text


# TODO функции не вызываем в принте

print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))
