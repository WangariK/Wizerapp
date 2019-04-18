import json
from difflib import get_close_matches


dictionary_data = json.load(open("data.json"))


def definitions(word):
    word = word.lower()
    if word in dictionary_data:
        return dictionary_data[word]

    elif word.title() in dictionary_data:
        return dictionary_data[word.title()]   # accounts for special nouns
    elif word.upper() in dictionary_data:
        return dictionary_data[word.upper()]   # checks for Acronyms

    elif len(get_close_matches(word, dictionary_data.keys())) > 0:
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no: " %
                       get_close_matches(word, dictionary_data.keys())[0])
        if choice == "Y":
            print('\n', "Word definition:")
            print(*dictionary_data[get_close_matches(word, dictionary_data.keys())[0]], sep='\n')

        elif choice == "N":
            return "Sorry the word doesn't exist or please double check it."

        else:
            return "We didn't understand your entry. Please try again."
    else:
        return "The word doesn't exist. Please double check it."


user_response = input("Enter word: ")
output = definitions(user_response)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
