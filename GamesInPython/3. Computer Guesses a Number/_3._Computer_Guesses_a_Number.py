import random

#def numberGuess(x):
#    #Generates a random number
#    randomNum = random.randint(1, x)
    
#    #Keeps track of number of guesses and instantiates myGuess
#    numberOfGuesses = 0;
#    myGuess = 0

#    #While loop that keeps track of number of guesses and myGuess
#    while (myGuess != randomNum) :
#        myGuess = int(input(f"Guess a number between 1 and {x}: "))
#        numberOfGuesses = numberOfGuesses+1

#        if myGuess > randomNum:
#            print ("Guess lower!")
#        elif myGuess < randomNum:
#            print ("Guess higher!")
    
#    #When I guess the number
#    print ("You guessed the number!")
#    print (f"It took you {numberOfGuesses} to get to the number.")

#x = int(input("Enter in a number, the higher the harder the game: "))
#numberGuess(x)

def computerGuess(x):
    low = 0
    high = x
    numberOfGuesses = 0;

    feedback = ""
    while feedback != "c":

        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)?").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

        numberOfGuesses += 1

    print(f"It took the computer {numberOfGuesses} to guess your number of {guess}!")


x = int(input("Enter in a number, the higher the harder the game for the computer: "))
print(f"Think of a number between 0 and {x}.\nYou know what, write it down on a piece of paper but don't show the computer.\nYou can't change it >:[.")
computerGuess(x)