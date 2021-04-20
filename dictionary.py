import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif: len(get_close_matches(w, data.keys())) > 0:
        return input("Did you mean %s instead? [Y=yes,N=no]: " % get_close_matches(w, data.keys)[0])
    else: 
        return "Sorry. That word doesn't exist. Please try a different word or try again."

word = raw_input("Enter a word you would like defined: ")

print(translate(word))

