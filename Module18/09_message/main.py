import re
text = re.findall(r"[\w']+|[-.:,!; ]", input('Сообщение: '))
print('Новое сообщение: ', *[word[::-1] for word in text], sep='')
