'''

created on: 14/09/2021
@author: saipradyumnanprem

'''

from random import randint

start = 1

end = 1000

value = randint(start, end)

print("Guess a value between {} and {}: ".format(start, end))

guess = None

while guess != value:
    guess = int(input("Guess the number: "))

    if guess < value:
        print("Guess Higher!")
    elif guess > value:
        print("Guess Lower!")

print("Congratulations! You hava guessed the right number.")

