'''

created on:
@author: saipradyumnanprem

'''

from random import randint

def game():
    dice = randint(1, 6)
    if dice == 1:
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------")

    elif dice == 2:
        print("-----------")
        print("|         |")
        print("| 0     0 |")
        print("|         |")
        print("-----------")

    elif dice == 3:
        print("-----------")
        print("|         |")
        print("| 0  0  0 |")
        print("|         |")
        print("-----------")

    elif dice == 4:
        print("-----------")
        print("| 0     0 |")
        print("|         |")
        print("| 0     0 |")
        print("-----------")

    elif dice == 5:
        print("-----------")
        print("| 0     0 |")
        print("|    0    |")
        print("| 0     0 |")
        print("-----------")

    elif dice == 6:
        print("-----------")
        print("| 0     0 |")
        print("| 0     0 |")
        print("| 0     0 |")
        print("-----------")



    choice = input("Do you want to roll the dice again? (y/n)")
    if choice == 'y' or choice == 'Y':
        game()



if __name__ == "__main__":
    game()
