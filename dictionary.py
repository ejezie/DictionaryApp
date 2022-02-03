import json
from difflib import get_close_matches
data = json.load(open("076 data.json", 'r'))


def dict(word):
    word = word.lower()

    if word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word, data.keys())) > 0:
        ask = input("did you mean? %s, type y if yes or n if no: " % get_close_matches(word, data.keys())[0])
        if ask == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif ask == 'n':
            return "please check your spelling"
        else:
            return "cannot understand your input"

    else:
        return 'incorrect word'


word = input('Enter word: ')
output = dict(word)

if type(output) is list:
    for item in output:
        print(item)
else:
    print(output)

print('done')
