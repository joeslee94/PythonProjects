import random

#Definitely want to add mindgames asking the user if they are sure
#Tell the user that the computer will throw out a certain one
#IF user inputs a winning letter, ask them to questions and give them a chance to reinput their choices
#Add a counter for streak of wins the user has

def RPS():
    yourMove = input("'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    compMove = random.choice(['r', 'p', 's'])
    
    if yourMove == compMove:
        print(f"It's a tie! With both of you throwing {yourMove}.")
        RPS()
    elif whoWins(yourMove, compMove):
        print(f"You won! You threw out {yourMove} and the computer threw out {compMove}.")
    else:
        print(f"Computer won :/. Comp threw out {compMove} and you threw out {yourMove}.")
    
    playAgain = input("'y' for Yes and 'n' for No: ")
    if playAgain == 'y':
        RPS()
    if playAgain == 'n':
        return 'Thanks for playing!'

def whoWins(yourMove, compMove):
    if (yourMove == 'r' and compMove == 's') or (yourMove == 'p' and compMove == 'r') or (yourMove == 's' and compMove == 'p'):
        return True

print(RPS())