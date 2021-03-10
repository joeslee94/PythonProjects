secretWord = "nasa"
guess = ""

guesscount = 0
guesslimit = 3
outofguesses = False

while guess != secretWord and not(outofguesses):
    if guesscount < guesslimit:
        guess = input("Enter in a word: ")
        guesscount += 1;
    else:
        outofguesses = True
    
if outofguesses == False:
    print("You win!")
else:
    print("You lose.")

