import random



name = input("Enter your name")
print("Welcome" , name )


d = random.choice(["pugger" , "littlepugger" , "tiger" , "superman" , "thor" , "pokemon" , "avengers" , "savewater" , "earth" , "annable" ])
word = list(d)
validLetters = 'abcdefghijklmnopqrstuvwxyz'







hidden = []
for character in word:    # this will take word and replace with _
    hidden.append("_")

attempts = 0
max_attempts = 4



isGameover = False
# loop until either the player has won or lost
while not isGameover:

    # display the current board, guessed letters, and attempts remaining

    print(f"You have {max_attempts-attempts} attempts remaining")

    print(f"the current word is :{' '.join(hidden)}") # Will display the _ with spaces ie upto length of word

    print("     ------")
    print("     |    |")
    print("     |    " + ("O" if attempts > 0 else ""))
    print("     |    " + ("/\\" if attempts > 1 else ""))
    print("     |    " + ("|" if attempts > 2 else ""))
    print("     |    " + ("/\\" if attempts > 3 else ""))
    print(" --------")





    guess = input("Please guess the word:")

    print('\n\n\n\n')


    if guess in validLetters:
        guessmade =  guess
    else:
        print("Enter a valid character")
        guess = input()

    if guessmade in word:
        # if the player guessed correct, show all matched letters and print message
        print(f"You guessed right {guessmade} is in the word")
        #Now if a letter is guessed right then replace hiddens _ with that letter and that word with __
        for i in range(len(word)): #run the loop for every word times of actuaol word
            b = word[i]             # every time story one alphabet in a variable
            if guessmade == b:
                hidden[i] = guessmade    # update the _ with that letters
                word[i] = "_"            # this step is important to avoid repetition of the already guessed alphabet

    else:

        # if player guessed wrong, print failure message and increment attempts
        print(f"You guessed wrong! {guessmade} is NOT in the word")
        #  to increase the number of attempts
        attempts += 1


    # if the player has won print a win message and stop looping
    # here the concept of all is that it sends you true or false based onthe list
    # the condition is simpe if all of the elements of word are _ then you win
    if all("_" == char for char in word):
        print("Congrats, you won!")
        break

    # if the player has lost, print failing and stop looping
    if attempts >= max_attempts:
        print("You lost, rest in peace!")
        break
