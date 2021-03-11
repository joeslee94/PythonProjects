import random
import string
from Words import Words

#provides a word without spaces or dashes so that the user can successfully guess letter
def noSpacesorDashes(Words):
    compRandomWord = random.choice(Words)
    
    while '-' in compRandomWord or ' ' in compRandomWord:
        compRandomWord = random.choice(Words)

    return compRandomWord.lower()

def hangMan():
    finalizedWord = noSpacesorDashes(Words) #gives us the word without dashes or spaces
    lettersInWord = set(finalizedWord) #HashSet that holds the unique letters within the word itself
    alphabet = set(string.ascii_lowercase) #alphabet set
    lettersGuessed = set() #holds letters that user has guessed
    chances = int(input('\nHow many chances do you want? Enter in a number: '))

    while (len(lettersInWord) > 0 and chances > 0):
        #displays the word with dashes of letters not guessed and letters where user guessed successfully
        finalizedWordList = [letter if letter in lettersGuessed else '-' for letter in finalizedWord]
        print('\n')
        print('Here is the word so far with the correct guesses: ',' '.join(finalizedWordList))
        print('\n')

        #tells user what letters they have already used AND num of chances
        print(f'You have {chances} chances left. ' + 'These are the letters you already guessed: ',' '.join(lettersGuessed))

        #asks the user to guess a letter
        playerLetterGuess = input('\nGuess a letter: ').lower()
        chances -= 1

        #Logic for the guesses and moving letters from 1 array to another
        if playerLetterGuess in alphabet - lettersGuessed:
            lettersGuessed.add(playerLetterGuess)
            if playerLetterGuess in lettersInWord:
                lettersInWord.remove(playerLetterGuess)

        elif playerLetterGuess in lettersGuessed:
            print("You already guessed that letter try again!")

        else:
            print("Invalid character.")
    
    if chances > 0:
        print(f'\nYou guessed the word correctly!\n'
              f'It took you {len(lettersGuessed)} guesses.\n'
              f'Here is the final word: {finalizedWord}.')
        if playAgain():
            hangMan()
    else:
        print(f'\nYou ran out of chances!\n'
              f'Here is the final word: {finalizedWord}.')
        if playAgain():
            hangMan()

def playAgain():
    yesOrNo = input('\nDo you want to play again? y for Yes, n for No: ')
    if yesOrNo == 'y':
        return True
    else:
        return False

print('Welcome to Guess My Word aka Hang Man')
hangMan()