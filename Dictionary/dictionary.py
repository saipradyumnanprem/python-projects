'''

created on:
@author: saipradyumnanprem

'''



import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(word):
    word = word.lower()

    if word in data:
        return data[word]

    elif word.title() in data:
        return data[word.title()]

    elif word.upper() in data:
        return data[word.upper()]

    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean {} instead?".format(get_close_matches(word, data.keys())[0]))
        decide = input("(y/n)?")
        if decide == "y" or decide == "Y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n" or decide == "N":
            return "Sorry! The word you are looking for may be incorrect / does not exist!"
        else:
            return "Please enter just y or n"

    else:
        return "Enter a valid word!"


if __name__ == "__main__":
    word = input("Enter the word you are looking for: ")

    output = translate(word)

    if type(output) == list:
        count = 1
        for item in output:
            print("{} : {}".format(count, item))
            count += 1
    else:
        print(output)