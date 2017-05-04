

text = input('Enter a string:').split()


DICTIONARY = {}

for word in text:
    DICTIONARY.update({word: str(text.count(word))})
sorted_DICTIONARY = sorted(DICTIONARY)

for word in sorted_DICTIONARY:
    print('{:{}} : {}'.format(word, len(max((DICTIONARY))), str(text.count(word))))


