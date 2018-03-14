import random

words = ["cheese","elephant","Gilmore Girls","netflix","apple juice"]

hint1 = ["food","big and fat animal","lorelai and rory","website","type of fruit juice"]

hint2 = ["mice like it","grey","stars hollow","movies and tv shows","made of a red fruit"]

number = random.randint(0,4)

secretword = words[number]

guess = ""

counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'first letter', 'last letter', or 'give up' for help.")
    guess = input()
    counter += 1

    if guess == secretword:
        print("You win! It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(  hint1[number]  )

    elif guess == "hint2":
        print( hint2[number] )

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "last letter":
        print( secretword[-1] )

    elif guess == "give up":
        print("The word was " + secretword)
        break






    
        
