import random

def numberGuess(x):
    #Generates a random number
    randomNum = random.randint(1, x)
    
    #Keeps track of number of guesses and instantiates myGuess
    numberOfGuesses = 0;
    myGuess = 0

    #While loop that keeps track of number of guesses and myGuess
    while (myGuess != randomNum) :
        myGuess = int(input(f"Guess a number between 1 and {x}: "))
        numberOfGuesses = numberOfGuesses+1

        if myGuess > randomNum:
            print ("Guess lower!")
        elif myGuess < randomNum:
            print ("Guess higher!")
    
    #When I guess the number
    print ("You guessed the number!")
    print (f"It took you {numberOfGuesses} to get to the number.")

x = int(input("Enter in a number, the higher the harder the game: "))
numberGuess(x)