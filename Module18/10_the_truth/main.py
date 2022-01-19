def encrypt(message):
    translated = ''
    for symbol in message:
        if symbol in letters:
            number = letters.find(symbol)
            translated += letters[number - 1]
        else:
            translated += symbol
    return translated


def shift(word, key_2):
    word_ln = len(word)
    offset = key_2 % word_ln
    word_new = word[-offset:] + word[:-offset]
    return word_new

text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

text_2 = []
key = 3
for i_word in text.split():
    text_decryption = encrypt(i_word)
    shift_text = shift(text_decryption, key)
    if shift_text.endswith("/"):
        key += 1
        text_2.append(shift_text)
    else:
        text_2.append(shift_text)

text_2 = " ".join(text_2)
text_2 = text_2.replace("+", "*")
text_2 = text_2.replace("-", ",")
text_2 = text_2.replace("(", "'")
text_2 = text_2.replace("..", "--")
text_2 = text_2.replace('"', "!")
text_2 = text_2.replace("/", ".\n")

print(text_2)
