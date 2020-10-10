import json
from difflib import get_close_matches

dict= json.load(open("dictionary.json"))


def lookup(x):
    x = x.lower()
    if x in dict:
        return dict[x]
    elif x.title() in dict:
        return dict[x.title()]
    elif x.upper() in dict:
        return dict[x.upper()]
    elif len(get_close_matches(x,dict.keys())) > 0 :
        print('did you mean %s' %get_close_matches(x,dict.keys())[0])
        a = input('press y for yes and n for no ')
        if a == "y":
            return dict[get_close_matches(x,dict.keys())[0]]
        else:
            return('you entered something wrong')


    else:
        print("your querry is not in the dictionary")



x = input('Enter your word here  ')
y = lookup(x)

if type(y) == list:
    for l in y:
        print(l)

else:
    print(y)
