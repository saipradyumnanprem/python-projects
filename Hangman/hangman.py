'''

created on:
@author: saipradyumnanprem

'''

import random


def hangman():
    namelist = ["movie", "cinema", "batman", "music"]
    word = random.choice(namelist)
    validletters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guessmade = ''

    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guessmade:
                main = main + letter
            else:
                main = main + "_" + " "

        if main == word:
            print(main)
            print("You Win! You guessed the right word!")
            break

        print("Guess the word: ", main)
        guess = input()

        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("Enter a valid character.")
            guess = input()

        if guess not in word:
            turns = turns - 1

            print("{} turns left! ".format(turns))

            if turns == 9:
                print(" ------------- ")

            if turns == 8:
                print(" ------------- ")
                print("       0       ")

            if turns == 7:
                print(" ------------- ")
                print("       0       ")
                print("       |       ")

            if turns == 6:
                print(" ------------- ")
                print("       0       ")
                print("       |       ")
                print("      /        ")

            if turns == 5:
                print(" ------------- ")
                print("       0       ")
                print("       |       ")
                print("      / \      ")

            if turns == 4:
                print(" ------------- ")
                print("     \ 0       ")
                print("       |       ")
                print("      / \      ")

            if turns == 3:
                print(" ------------- ")
                print("     \ 0 /     ")
                print("       |       ")
                print("      / \      ")

            if turns == 2:
                print(" ------------- ")
                print("     \ 0 /|    ")
                print("       |       ")
                print("      / \      ")

            if turns == 1:
                print("Last breath! Tread Carefully!")
                print(" ------------- ")
                print("     \ 0_|/    ")
                print("       |       ")
                print("      / \      ")

            if turns == 0:
                print("You Lose! You let the man die!")
                print(" ------------- ")
                print("       0_|     ")
                print("      /|\      ")
                print("      / \      ")

if __name__ == "__main__":
    name = input("Enter your name: ")
    print("Welcome {}, to Hangman Game.".format(name.title()))
    print("--------------------------" + "-" * len(name))
    print("Guess the word in less than 10 tries!")
    hangman()


