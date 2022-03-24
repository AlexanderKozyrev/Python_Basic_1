alfavit_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alfavit_2 = alfavit_1.lower()
file = open('cipher_text.txt', 'a')
smeshenie = 1
text = open('text.txt', 'r')

for line in text:
    word = ''
    for letter in line:
        if letter in alfavit_1:
            mesto = alfavit_1.find(letter)
            word += alfavit_1[mesto + smeshenie]
        elif letter in alfavit_2:
            mesto = alfavit_2.find(letter)
            word += alfavit_2[mesto + smeshenie]
        else:
            word += letter
    file.write(word)
    smeshenie += 1
file.close()
text.close()