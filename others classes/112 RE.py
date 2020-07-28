import re
'''Exemplo 1
patterns = ['term1', 'term2']

text = 'This is a string with term1, not not the other!'


for pattern in patterns:
    print("I'm searching for: "+pattern)

    if re.search(pattern, text):
        print("Match!")
    else:
        print("No match...")
'''

def multi_re_find(patterns, phrase):


    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')


test_phrase = 'sdsd..sssddd..sdddsddd...dsds...dssssss...sddddd'

test_patterns = ['s+d?']

multi_re_find(test_patterns, test_phrase)
