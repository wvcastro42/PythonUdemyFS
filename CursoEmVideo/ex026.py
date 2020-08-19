phrase = input('Type some phrase: ').strip().lower()

print('Times that letter A appears: {}'.format(phrase.count('a')))
print('First position that letter A appears: {}'.format(phrase.find('a')))
print('Last position that letter A appears: {}'.format(phrase.rfind('a')))
