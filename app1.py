#interactive dictionary application
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:              #for words like Delhi,Mumbai etc.
        return data[x.title()]
    elif x.upper() in data:              #for words like USA etc.
        return data[x.upper()]       
    elif len(get_close_matches(x,data.keys())) >0:
        show = input("Did you mean %s instead. If yes than type Y or if no then type N:" % get_close_matches(x,data.keys())[0])
        if show == "y":
            return data[get_close_matches(x, data.keys())[0]]
        elif show == "n":
            return "The word does not exists. Please check it once."
        else:
            return "we din't understand your entry."            
    else:
        return "This word does not exist.Please check it once."  

word = input("enter word: ")
output = translate(word)
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)          





