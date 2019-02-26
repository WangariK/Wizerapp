import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]   # accounts for special nouns
    elif word.upper() in data:
        return data[word.upper()]   # checks for Acronyms

    elif len(get_close_matches(word, data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                       get_close_matches(word, data.keys())[0])
        if choice == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif choice == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry. Please try again."
    else:
        return "The word doesn't exist. Please double check it."


user_response = input("Enter word: ")
output = translate(user_response)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
