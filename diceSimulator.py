import random

print("This is a dice stimulator")

x="y"

while x=="y":
    numGen = random.randint(1,6)

    if numGen== 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if numGen== 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if numGen == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if numGen == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if numGen == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if numGen == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")

    x= input("press Y to continue and anyother to cancel program")
